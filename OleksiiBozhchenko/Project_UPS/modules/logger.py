import os
from configuration.config import *
from configuration.credentials import *

def log_nonify(message):
    with open(os.getcwd() + LOG_FILE, "a", encoding = "utf-8") as my_file:
        my_file.write(message + "\n")
