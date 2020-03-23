import logging
import os
import sys
from dotenv import load_dotenv, find_dotenv
from app.config import settings

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.\
                        format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger()

ENV_APP = os.environ.get('ENV_APP')
ENV_APP = ENV_APP[:1].upper() + ENV_APP[1:].lower()

_current = getattr(sys.modules['app.config.settings'], '{0}Config'.format(ENV_APP))()
for atr in [f for f in dir(_current) if not '__' in f]:
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)