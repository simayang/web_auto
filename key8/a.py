"""
context 上下文环境  (解决多账号同时登录的问题）
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False,channel="chrome")
    context1 = browser.new_context()
    context2 = browser.new_context()
    # 建立两套不同的上下文，打开标签页
    page1 = context1.new_page()
    page2 = context2.new_page()

    # page1登录
    page1.goto("http://47.116.12.183/login.html")
    page1.get_by_placeholder("请输入用户名").fill("test")
    page1.get_by_placeholder("请输入密码").fill("123456")
    page1.get_by_text("立即登录").click()
    page1.wait_for_timeout(5000)

    # page2登录
    page2.goto("http://47.116.12.183/login.html")
    page2.get_by_placeholder("请输入用户名").fill("test1")
    page2.get_by_placeholder("请输入密码").fill("123456")
    page2.get_by_text("立即登录").click()
    page2.wait_for_timeout(5000)

    page1.pause()
    page2.pause()