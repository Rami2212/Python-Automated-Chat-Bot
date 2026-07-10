from .config import CHAT_URL, USER_NAME, IFRAME_URL

def login(page):
    page.goto(CHAT_URL, timeout=100000)

    # Wait for iframe to appear
    page.wait_for_selector("iframe", timeout=100000)  

    # Get the frame by URL
    frame = page.frame(url=IFRAME_URL)
    if frame is None:
        print("Frame not found!")
        return

    # Fill username and click login
    frame.fill(".arrowchat_guest_name_input", USER_NAME)
    frame.click("#arrowchat_guest_name_button")

    # Wait for chat textarea
    frame.wait_for_selector(".arrowchat_textarea", timeout=100000)
    print("Logged in")