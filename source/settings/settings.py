from pathlib import Path
from utils import get_env_var

BASE_DIR = Path(__file__).parent.parent.parent
DRIVER_PATH = BASE_DIR / get_env_var('DRIVER_PATH')

API_ID = get_env_var('API_ID')
APP_HASH = get_env_var('APP_HASH')
SESSION_PATH = BASE_DIR / 'anonymous'
