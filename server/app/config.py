from datetime import timedelta, timezone
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRETE_KEY = environ.get("SECRETE_KEY")
    TIME_ZONE = timezone(timedelta(minutes=int(environ.get("TZ_OFFSET", "210"))))
    JWT_EXP_TIMEDELTA = timedelta(minutes=int(environ.get("TOKEN_EXP", "20")))
    JWT_ALGORITHM = "HS256"


config = Config()
