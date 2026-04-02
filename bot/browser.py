from playwright.sync_api import sync_playwright

def launch_browser(headless=False):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    page = browser.new_page()
    return p, browser, page