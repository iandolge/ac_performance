import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    ADMINS = [os.environ.get("ADMINS")]
