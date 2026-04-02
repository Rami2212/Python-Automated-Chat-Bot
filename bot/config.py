import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
CHAT_URL = os.getenv("CHAT_URL")
IFRAME_URL = os.getenv("IFRAME_URL")
TARGET_LINK = os.getenv("TARGET_LINK")
M1 = os.getenv("M1")
M2 = os.getenv("M2")

HEADLESS = False
MIN_DELAY = 180
MAX_DELAY = 300