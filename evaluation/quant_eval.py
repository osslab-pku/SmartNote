import os
import pandas as pd
from glob import glob
import re
import textstat
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from config import init_env, settings
from github import Github
from tqdm import tqdm
from math import log2
from functools import lru_cache
import tiktoken

init_env('evaluation')

gh = Github(settings.GITHUB_TOKEN)
tokenizer = AutoTokenizer.from_pretrained("taidng/wikiser-bert-base")
model = AutoModelForTokenClassification.from_pretrained("taidng/wikiser-bert-base")

nlp = pipeline("ner", model=model, tokenizer=tokenizer, device=settings.TORCH_DEVICE)

SHA_REGEX = re.compile(r'([0-9a-f]{7,40})')
PR_NUMBER_REGEX = re.compile(r'#(\d+)')
PR_URL_REGEX = re.compile(r'/pull/(\d+)')
REGEX_NAME = re.compile(r'-- ([\w-]+)/([\w-]+)')
REGEX_VERSION = re.compile(r'--previous-release\s+(\S+) --current-release\s+(\S+)')

def clean_text(s : str) -> str:
    '''
    Removes formatting and other non-content data that may skew compression ratios (e.g., duplicate spaces)
    '''
    # Remove extra spaces and duplicate newlines.
    s = re.sub(' +', ' ', s)
    s = re.sub('\t', '', s)
    s = re.sub('\n+', '\n', s)
    s = re.sub('\n ', '\n', s)
    s = re.sub(' \n', '\n', s)

    # Remove non-alphanumeric chars
    s = re.sub(r'[^0-9A-Za-z,\.\(\) \n]', '', s)

    return s

@lru_cache
def _get_commits_and_prs_between_versions(
        name_with_owner: str,
        from_version: str,
        to_version: str,
):
    gh_repo = gh.get_repo(name_with_owner)
    # get commits list
    _commits = list(gh_repo.compare(from_version, to_version).commits)
    _pr_to_commits = {}
    
    for c in tqdm(_commits):
        for pr in gh_repo.get_commit(c.sha).get_pulls():
            _pr_to_commits[pr.number] = _pr_to_commits.get(pr.number, []) + [c]
    
    return _pr_to_commits, _commits

def _match_commits_and_prs(
        rn_md: str,
):
    _commits = SHA_REGEX.findall(rn_md)
    _prs = PR_NUMBER_REGEX.findall(rn_md)
    _pr_urls = PR_URL_REGEX.findall(rn_md)
    return (
        set(_c[:7] for _c in _commits),
        set(int(p) for p in _prs) | set(int(p) for p in _pr_urls),
    )

def calculate_commit_coverage(
        name_with_owner: str,
        from_version: str,
        to_version: str,
        rn_md: str,
):
    _pr_to_commits, _commits_to_hit = _get_commits_and_prs_between_versions(name_with_owner, from_version, to_version)
    # replace all commits objects with short sha
    _commits_to_hit = set(c.sha[:7] for c in _commits_to_hit)
    _n_commits = len(_commits_to_hit)
    _pr_to_commits = {k: [c.sha[:7] for c in v] for k, v in _pr_to_commits.items()}

    #print("PRs", _pr_to_commits, "Commits", _commits_to_hit)

    _commits_in_rn, _prs_in_rn = _match_commits_and_prs(rn_md)
    for c in _commits_in_rn:
        if c in _commits_to_hit:
            _commits_to_hit.remove(c)
    for pr in _prs_in_rn:
        if pr in _pr_to_commits:
            _commits_to_hit -= set(_pr_to_commits[pr])

    return 1 - len(_commits_to_hit) / _n_commits

def count_info_entropy(md: str):
    """
    Count the information entropy of a markdown release note.
    """
    lines = md.split('\n')
    _entries_cnt = []
    _curr_cnt = 0
    for l in lines:
        if l.strip().startswith('#'):
            _entries_cnt.append(_curr_cnt)
            _curr_cnt = 0
        elif l.strip().startswith('-') or l.strip().startswith('*'):
            _curr_cnt += 1
    _entries_cnt.append(_curr_cnt)
    _sum = sum(_entries_cnt)
    _ent = 0
    for ent in _entries_cnt[1:]:
        if ent == 0:
            continue
        _ent += (ent / _sum) * log2(ent / _sum)

    # convert 0.0 to -0.0
    if _ent == 0.0:
        return 0.0
    return -_ent

def parse_cli_args(s: str):
    # yields an error if unmatched, should never happen
    repo_name = REGEX_NAME.search(s).group(1) + '/' + REGEX_NAME.search(s).group(2)
    from_version = REGEX_VERSION.search(s).group(1)
    to_version = REGEX_VERSION.search(s).group(2)
    return repo_name, from_version, to_version

def entity_density(text: str) -> int:
    return len(nlp(text)) / len(tokenizer(text)['input_ids'])

@lru_cache
def get_tokenizer(model_name: str) -> tiktoken:
    return tiktoken.encoding_for_model(model_name)

def count_tokens(text: str, model_name: str = "gpt-4o") -> int:
    tokenizer = get_tokenizer(model_name)
    return len(tokenizer.encode(text, disallowed_special=()))

def eval_path(out_path):
    _cli_file_path = os.path.join(out_path, 'details.txt')

    repo_name, from_version, to_version = parse_cli_args(open(_cli_file_path).read())
    repo_name, from_version, to_version

    # list markdown files
    _markdown_files = [f for f in os.listdir(out_path) if f.endswith('.md')]

    results = []
    for _f in _markdown_files:
        print(f'Processing {_f}...')
        _rn_md = open(os.path.join(out_path, _f)).read()
        results.append({
            'repo_name': repo_name,
            'rn_name': _f.replace('.md', ''),
            'commit_coverage': calculate_commit_coverage(repo_name, from_version, to_version, _rn_md),
            'info_entropy': count_info_entropy(_rn_md),
            'tokens_count': count_tokens(_rn_md),
            # 'llm_brotli': det_br.score_text(_rn_md),
            # 'llm_lzma': det_lzma.score_text(_rn_md),
            # 'reading_ease': textstat.flesch_reading_ease(clean_text(_rn_md)),
            'automated_readability_index': textstat.automated_readability_index(clean_text(_rn_md)),
            'dale_chall_readability': textstat.dale_chall_readability_score(clean_text(_rn_md)),
            # 'smog_readability': textstat.smog_index(clean_text(_rn_md)),
            # 'coleman_liau_index': textstat.coleman_liau_index(clean_text(_rn_md)),
            'entity_percent': entity_density(clean_text(_rn_md)) * 100,
            # 'entity_count': len(nlp(clean_text(_rn_md))),
        })

    return pd.DataFrame(results)

if __name__ == '__main__':
    _l_ev = []
    for out_path in glob('*/*'):
        if 'node_modules' in out_path:
            continue
        if not os.path.exists(os.path.join(out_path, 'details.txt')):
            continue
        print(f'Processing {out_path}...')
        df_rn = eval_path(out_path)
        df_rn['project_domain'] = out_path.split('/')[0]
        df_rn.to_csv(os.path.join(out_path, 'quant_eval.csv'), index=False)
        _l_ev.append(df_rn)

    df_ev = pd.concat(_l_ev)
    df_ev.to_csv('quant_eval.csv', index=False)