from config import config
from datetime import datetime
def now():
    return datetime.now(tz=config.TIME_ZONE)