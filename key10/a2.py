"""
断言打开新页面
"""

from playwright.sync_api import sync_playwright,expect
import re
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("https://www.baidu.com/", wait_until="networkidle")

    # 显示断言打开了新的tab标签页
    with page.expect_popup() as new:
        page.click("text=hao123",timeout=3000)
    new_page = new.value

    # 断言新窗口
    expect(new_page).to_have_title("ao123_上网从这里开始",timeout=5000)
    new_page.close() # 关闭新窗口

    page.pause()