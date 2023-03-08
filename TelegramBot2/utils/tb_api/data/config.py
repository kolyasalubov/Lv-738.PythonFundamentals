import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("5922482735:AAEYOC_ohtA5TG8kYQkp9nP6WJ3nfib4-a4"))

admins_id = [
    391585190

]


ip = os.getenv("ip")
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE =str(os.getenv("DATABASE"))

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
