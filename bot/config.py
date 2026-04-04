import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
CHAT_URL = os.getenv("CHAT_URL")
IFRAME_URL = os.getenv("IFRAME_URL")

CHAT_MODE = os.getenv("CHAT_MODE")

M1 = ""
M2 = ""
M = ""

if CHAT_MODE == "c":
    TARGET_LINK = os.getenv("TARGET_LINK")
    M1 = os.getenv("M1")
    M2 = os.getenv("M2")
elif CHAT_MODE == "v":
    TARGET_LINK = os.getenv("TARGET_LINK_VIDEO")
    M1 = os.getenv("M2")
    M2 = os.getenv("M3")
else:
    TARGET_LINK = [os.getenv("TARGET_LINK"),
                   os.getenv("TARGET_LINK_VIDEO")]
    M = [os.getenv("M1"),
         os.getenv("M2"),
         os.getenv("M3")]

CHAT_TIMER = int(os.getenv("CHAT_TIMER"))

if CHAT_TIMER == 1:
    MIN_DELAY = 20
    MAX_DELAY = 40
elif CHAT_TIMER == 2:
    MIN_DELAY = 30
    MAX_DELAY = 60
elif CHAT_TIMER == 3:
    MIN_DELAY = 60
    MAX_DELAY = 120
elif CHAT_TIMER == 4:
    MIN_DELAY = 200
    MAX_DELAY = 300

HEADLESS = False
