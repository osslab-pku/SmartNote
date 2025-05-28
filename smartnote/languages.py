import yaml
import numpy as np
import os

with open(os.path.join(os.path.dirname(__file__), 'languages.yml')) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    
FILENAME_TO_LANG = {}
FILENAME_TO_LANGID = {}
LANG_NAMES = {}

for lang, lang_data in data.items():
    # remove niche languages, whose language_id is not contiuous
    # TODO: currently it leaves out some niche languages and ignores extension overlaps (e.g. .m), should be fine in common cases
    if lang_data.get('language_id') > 1000:
        continue
    LANG_NAMES[lang_data['language_id']] = lang
    if 'extensions' in lang_data:
        for ext in lang_data['extensions']:
            FILENAME_TO_LANG[ext] = lang
            FILENAME_TO_LANGID[ext] = lang_data['language_id']
    if 'filenames' in lang_data:
        for filename in lang_data['filenames']:
            FILENAME_TO_LANG[filename] = lang
            FILENAME_TO_LANGID[filename] = lang_data['language_id']

MAX_LANG_ID = max(FILENAME_TO_LANGID.values())

def get_lang_name(lang_id: int) -> str:
    if lang_id == MAX_LANG_ID + 1:
        return 'unknown'
    if lang_id in LANG_NAMES:
        return ''.join(w.title() for w in LANG_NAMES[lang_id].split(' '))
    return str(lang_id)

def get_lang_names(prefix='lang') -> list[str]:
    return [f"{prefix}{get_lang_name(lang_id)}" for lang_id in range(MAX_LANG_ID + 1)]

def infer_lang(filename: str) -> str:
    if filename in FILENAME_TO_LANG:
        return FILENAME_TO_LANG[filename]
    ext = '.' + filename.split('.')[-1]
    if ext in FILENAME_TO_LANG:
        return FILENAME_TO_LANG[ext]
    return 'Unknown'

def infer_lang_id(filename: str) -> int:
    if filename in FILENAME_TO_LANGID:
        return FILENAME_TO_LANGID[filename]
    ext = '.' + filename.split('.')[-1]
    if ext in FILENAME_TO_LANGID:
        return FILENAME_TO_LANGID[ext]
    return -1  # this works because -1 is a valid index in Python

def infer_langids_onehot(filenames: list[str]) -> np.ndarray:
    onehot = np.zeros(MAX_LANG_ID + 2, dtype=np.int8)
    for lang in filenames:
        ext = '.' + lang.split('.')[-1]
        if lang_id := FILENAME_TO_LANGID.get(lang):
            onehot[lang_id] = 1
        elif lang_id := FILENAME_TO_LANGID.get(ext):
            onehot[lang_id] = 1
        else:
            onehot[MAX_LANG_ID + 1] = 1
    return onehot