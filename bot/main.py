from .browser import launch_browser
from .auth import login
from .chat import send_message
from .config import HEADLESS

def run():
    p, browser, page = launch_browser(headless=HEADLESS)

    try:
        login(page)

        while True:
            send_message(page)

    except KeyboardInterrupt:
        print("Stopped by user")

    finally:
        browser.close()
        p.stop()

if __name__ == "__main__":
    run()