import random
from .message import MESSAGES
from .utils import random_delay
from .config import IFRAME_URL, MIN_DELAY, MAX_DELAY

def send_message(page):
    message = random.choice(MESSAGES)

    # Wait for iframe to appear
    page.wait_for_selector("iframe")

    # Get the frame by URL
    frame = page.frame(url=IFRAME_URL)
    if frame is None:
        print("Frame not found!")
        return

    frame.fill(".arrowchat_textarea", message)
    frame.click(".arrowchat_user_send_button")

    print("Sent:", message)
    random_delay(MIN_DELAY, MAX_DELAY)
