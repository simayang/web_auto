"""
鼠标滚动 https://www.jianshu.com/

鼠标滚轮操作调用page.mouse.wheel() 方法:
    • delta_x 横向移动距离
    • delta_y 纵向移动距离
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("https://www.jianshu.com/", wait_until="networkidle")

    for i in range(10):
        page.mouse.wheel(0,500)
        page.wait_for_timeout(1000)

    page.pause()
