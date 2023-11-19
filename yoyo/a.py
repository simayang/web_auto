from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('file:///C:/Users/dell/Desktop/a2/t.html')

    # 点击success按钮
    page.locator('.btn-success').click()

    # 如何判断消息框弹出来了
    # if page.locator('.toast-message').is_visible():
    #     print("消息框弹出来了。。。。")
    expect(page.locator('.toast-message')).to_be_visible(timeout=1000)

    page.pause()


