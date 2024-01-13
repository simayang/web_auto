"""
多窗口（多标签页）的切换 -- 第二种方式，事件监听
"""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://www.baidu.com/")

    with page1.expect_popup() as new_pp:
        page1.get_by_text("hao123").click()
    new_p = new_pp.value
    print(new_p.url)
    print(new_p.title())

    # 事件监听函数
    def handle_page(page):
        page.wait_for_load_state()
        print(page.title())
    context1.on("page1", handle_page)




