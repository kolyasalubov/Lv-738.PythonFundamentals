import os
# import subprocess
from configuration.config import SHUTDOWN
from configuration.credentials import HOST_USER


def get_service_status(REQUEST_STATUS):
    return os.popen(REQUEST_STATUS).read()
    # return subprocess.Popen(REQUEST_STATUS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# function for test
def get_file_status(REQUEST_FILE):
    with open(os.getcwd() + REQUEST_FILE, "r", encoding = "utf-8") as f:
        return f.read()

def get_ping(ip):
    return os.popen("ping -c 3 {}".format(ip)).read()
    # return str(subprocess.Popen("ping -c 3 {}".format(ip), shell=True))

def shutdown(ip):
    os.popen("ssh {}@{} {}".format(HOST_USER, ip, SHUTDOWN))
    # subprocess.Popen(f"ssh {HOST_USER}@{ip} {SHUTDOWN}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
