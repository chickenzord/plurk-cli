import os
from plurk_oauth.PlurkAPI import PlurkAPI
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PLURK_APP_KEY = os.environ.get("PLURK_APP_KEY")
PLURK_APP_SECRET = os.environ.get("PLURK_APP_SECRET")
PLURK_TOKEN = os.environ.get("PLURK_TOKEN")
PLURK_TOKEN_SECRET = os.environ.get("PLURK_TOKEN_SECRET")

def init():
    return PlurkAPI(PLURK_APP_KEY, PLURK_APP_SECRET, PLURK_TOKEN, PLURK_TOKEN_SECRET)
