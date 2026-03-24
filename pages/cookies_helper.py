import json

def save_cookies(browser, filename="cookies.json"):
    cookies = browser.get_cookies()
    with open(filename, "w") as f:
        json.dump(cookies, f)

def load_cookies(browser, filename="cookies.json"):
    with open(filename, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        browser.add_cookie(cookie)
