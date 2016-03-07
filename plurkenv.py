import os
from plurk_oauth.PlurkAPI import PlurkAPI
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
APP_TOKEN = os.environ.get("APP_TOKEN")
APP_SECRET = os.environ.get("APP_SECRET")

def init(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, app_token = APP_TOKEN, app_secret = APP_SECRET):
    return PlurkAPI(consumer_key, consumer_secret, app_token, app_secret)
