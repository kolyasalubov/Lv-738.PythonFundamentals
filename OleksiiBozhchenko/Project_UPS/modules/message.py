import datetime

def make_message(detail):
    result = str(f"{datetime.datetime.now()} {detail}")
    return result