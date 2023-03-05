import requests
from configuration.config import *
from configuration.credentials import *

def discord_notify(message):
        requests.post(f"{DISCORD_URL}/{DISCORD_ID}/{DISCORD_TOKEN}", data = {'content': message})

