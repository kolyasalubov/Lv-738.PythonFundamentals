import subprocess
from modules.logger import *
from configuration.config import *
from configuration.credentials import *

def constant_validation():
    check_service()
    check_host()
    check_status()
    check_timer()
    check_discord()

def check_service():
    try:
        # p = os.popen("service nut status").read()
        p = subprocess.Popen("service nut status", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if "active (running)" not in str(p):
            raise ValueError("Service NUT is not running")
    except(ValueError) as e:
        log_nonify(str(e))
        

def check_host():
    try:
        if not HOST or not isinstance(HOST, list):
            raise ValueError("HOST is empty or has wrong format. Must be data type \"list\"")
        else:   
            for i in HOST:
                k = i.split(".")
                for j in k:
                    if int(j) not in range(0,255):
                        raise ValueError(f"{j} in IP {i} in HOSTS is wrong")   
    except(ValueError) as e:
        log_nonify(str(e))              

def check_status():
    try:
        if not STATUS_ONBATTERY or not isinstance(STATUS_ONBATTERY, str):
            raise ValueError("REQUEST_ONBATTERY is empty or must be data type \"string\"")
        if not STATUS_ONLINE or not isinstance(STATUS_ONLINE, str):
            raise ValueError("REQUEST_ONLINE  is empty or must be data type \"string\"")
    except(ValueError) as e:
        log_nonify(str(e))

def check_timer():
    try:
        if not TIME_POOLING or not isinstance(TIME_POOLING, int) or TIME_POOLING <=0:
            ValueError("TIME_POOLING must have a natural number")
        if not TIME_DELAY or not isinstance(TIME_DELAY, int) or TIME_DELAY <= 0:
            ValueError("TIME_DELAY must have a natural number")
        if not PING_TIMES or not isinstance(PING_TIMES, int) or PING_TIMES <= 0:
            ValueError("PING_TIMES must have a natural number")
    except(ValueError) as e:
        log_nonify(str(e))

def check_discord():
    try:
        if not DISCORD_ID or not isinstance(DISCORD_ID, str):
            ValueError("DISCORD_ID is empty or has wrong format. Must be data type \"string\"")
        if not DISCORD_TOKEN or not isinstance(DISCORD_TOKEN, str):
            ValueError("DISCORD_TOKEN is empty or has wrong format. Must be data type \"string\"")
        if not DISCORD_URL or not isinstance(DISCORD_URL, str):
            ValueError("DISCORD_URL is empty or has wrong format. Must be data type \"string\"")
    except(ValueError) as e:
        log_nonify(str(e))


