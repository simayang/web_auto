"""
输入文本
locator.fill("一段文本")
locator.type('一个个的输入')

键盘操作 (备用，当前面2个无效的时候)
page.keyboard.type("Hello World!")
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("http://47.116.12.183/login.html", wait_until="networkidle")
    # 先登录
    page.get_by_placeholder("请输入用户名").click()

    # type
    page.keyboard.type("Hello World!")

    # press ("要按下的键"),按下哪个键
    # 按键盘上的删除
    page.keyboard.press("Backspace")
    # 再按下键盘上的回车
    page.keyboard.press("Enter")

    page.pause()