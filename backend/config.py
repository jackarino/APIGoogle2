# backend/config.py
import os


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")
