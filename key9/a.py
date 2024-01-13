"""
鼠标悬停：hover
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser =  p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("https://www.baidu.com/")

    # 鼠标悬停
    # exact = True 是精确匹配
    page.locator('#s-usersetting-top').hover()
    page.get_by_text("高级搜索",exact=True).click()
    page.pause()

