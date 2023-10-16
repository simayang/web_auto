"""
等待时间
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page() # 打开标签页
    page.goto("https://www.baidu.com")
    print(page.title()) # 打印当前页title

    page.locator('#kw').fill("司马")
    page.wait_for_timeout(3000) # 单位是毫秒

    # 运行完成后结束
    page.close() # 关闭浏览器标签
    browser.close() #关闭浏览器对象

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False,channel="chrome",slow_mo=3000)
#     page = browser.new_page() # 打开标签页
#     page.goto("https://www.baidu.com")
#     print(page.title()) # 打印当前页title
#
#     page.locator('#kw').fill("司马")
#
#     # 运行完成后结束
#     page.close() # 关闭浏览器标签
#     browser.close() #关闭浏览器对象