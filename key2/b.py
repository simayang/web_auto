from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.108.155.10/login.html")

    # page.locator("text=没有账号？点这注册").click()
    # 文本 默认 包含即模糊匹配文本 get_by_text()通过文本内容定位。
    # page.get_by_text("没有账号？").click()
    # 精确匹配
    # page.get_by_text("没有账号？点这注册",exact=True).click()

    # get_by_label("用 户 名:").fill("yoyo")
    page.get_by_label("用 户 名:").fill("yoyo")
    # page.get_by_label("密     码:").fill("aa123456")
    page.get_by_placeholder("请输入密码").fill("aa123456")

    page.get_by_text("立即登录").click()


    page.pause()