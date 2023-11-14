"""
网易云课程，定位登录

"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False,channel="chrome")
    # 新开标签页
    page = browser.new_page()
    # 打开网站
    page.goto("https://study.163.com/")
    # 点击登录/注册、点击邮箱登录
    page.get_by_text("登录/注册").click()
    page.get_by_text("邮箱登录").click()

    # 定位iframe
    frame = page.frame_locator("#j-ursContainer-0 iframe[id^=x-URS-iframe]")

    # 使用iframe定位它下面的元素
    frame.get_by_placeholder("网易邮箱/常用邮箱").fill("123")
    # 打断点
    page.pause()