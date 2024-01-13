"""
多窗口（多标签页）的切换 -- 第一种方式下标取值
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://www.baidu.com/")

    page1.get_by_text("hao123").click()

    print(page1.title())
    print(page1.url)
    page1.wait_for_timeout(3000)
    # 方式1：下标取值
    print(context1.pages) # 列表形式取到所有标签页，注意前面运行太快可能拿不到所有的，需要在前面加等待时间
    print(context1.pages[0])
    print(context1.pages[-1])
    print(context1.pages[-1].title())
    page1.pause()


