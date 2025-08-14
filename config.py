import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "instance", "urlshort.db")
    # You can add other settings like:
    # DEBUG = True
