from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome',headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com/")
    page.locator('#s-usersetting-top').hover() # hover 鼠标悬停
    page.pause()