"""
context 创建多个标签页
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    context1 = browser.new_context()

    # page1 登录
    page1 = context1.new_page() # new_page 打开标签页
    page1.goto("http://47.116.12.183/login.html")

    # page2 打开百度
    page2 = context1.new_page()
    page2.goto("https://www.baidu.com")

    page1.get_by_placeholder("请输入用户名").fill("test")
    page1.get_by_placeholder("请输入密码").fill("123456")
    page1.get_by_text("立即登录").click()
    page1.wait_for_timeout(5000)

    page1.pause()