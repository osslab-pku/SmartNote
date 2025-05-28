import os
from typing import Literal, List, Union
from dynaconf import Dynaconf
from pathlib import Path
from loguru import logger

settings = None

def load_settings():
    global settings
    settings = Dynaconf(
        envvar_prefix="SMARTNOTE",
        settings_files=['settings.toml', '.secrets.toml'],
        merge_enabled=True,
    )

load_settings()

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

def get_path(type: Literal['plots','models','datasets','cache','results'], name: str = '') -> Path:
    _path = settings.paths[type]
    if name:
        _path = os.path.join(_path, name)
    _basepath = Path(__file__).resolve().parent
    _path = os.path.join(_basepath, _path)
    os.makedirs(_path, exist_ok=True)
    return Path(_path)


def _mask(s: str) -> str:
    _len = max(3, len(s) // 5)
    return '*' * (len(s) - _len) + s[-_len:]

def _check_github_token(token: str) -> bool:
    import requests
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    r = requests.get('https://api.github.com/user', headers=headers)
    if not r.ok:
        logger.info(f'Invalid token: {_mask(token)}')
        return False
    return True

def _ensure_cuda_devices(cuda_devices: Union[str, List[str], None] = None):
    if cuda_devices is not None:
        if isinstance(cuda_devices, list):
            cuda_devices = ','.join([str(d) for d in cuda_devices])
        os.environ['CUDA_VISIBLE_DEVICES'] = str(cuda_devices)
    
    import torch
    if torch.cuda.is_available():
        _torch_device = torch.device('cuda')
        logger.info(f'CUDA is available, using GPU {torch.cuda.get_device_name()} x'
                f'{torch.cuda.device_count()}')
    else:
        _torch_device = torch.device('cpu')
        logger.info('CUDA is not available, switching to CPU')

    return _torch_device

def init_env(name='', 
         cuda_devices: Union[str, List[str], None] = None, 
         seed=19260817):
    
    global settings

    # ensure paths
    settings.PLOTS_PATH = get_path('plots', name)
    settings.MODELS_PATH = get_path('models', name)
    settings.DATASETS_PATH = get_path('datasets')
    settings.CACHE_PATH = get_path('cache', name)

    # set hf env
    _base_path = os.path.dirname(settings.DATASETS_PATH)
    os.environ['HF_HOME'] = get_path('cache').as_posix()
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # set tiktoken env
    os.environ['TIKTOKEN_CACHE_DIR'] = get_path('cache').as_posix()

    # init proxy
    try:
        os.environ['HTTPS_PROXY'] = settings.proxy.https
    except (KeyError, AttributeError):
        pass
    
    # cuda devices
    settings.TORCH_DEVICE = _ensure_cuda_devices(cuda_devices)
    # mute tokenizers fork warning
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    
    # seed everything
    settings.SEED = seed
    import numpy as np
    import torch
    np.random.seed(settings.SEED)
    torch.manual_seed(settings.SEED)
    
    # check tokens
    _tokens_list = [settings.github.token]
    if hasattr(settings.github, 'tokens'):
        _tokens_list += settings.github.tokens
    _valid_tokens = list(filter(_check_github_token, _tokens_list))
    if not _valid_tokens:
        raise ValueError('No valid GitHub tokens found')
    settings.GITHUB_TOKENS = _valid_tokens
    settings.GITHUB_TOKEN = settings.GITHUB_TOKENS[0]

    # silent pandas performance warning
    import pandas as pd
    import warnings
    warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

def manual_gc():
    # run gc
    import gc
    gc.collect()
    import torch
    torch.cuda.empty_cache()