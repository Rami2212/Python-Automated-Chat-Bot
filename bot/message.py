from .config import M1, M2, TARGET_LINK, M, CHAT_MODE

if CHAT_MODE == "b":
    MESSAGE_CONFIG = {"mode": "b", "links": TARGET_LINK, "messages": M}
else:
    MESSAGE_CONFIG = {"mode": "other", "data": [(TARGET_LINK, M1), (TARGET_LINK, M2)]}