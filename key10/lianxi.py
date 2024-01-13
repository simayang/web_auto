from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("http://47.116.12.183/register.html", wait_until="networkidle")

    # locator方式点击
    # page.locator("text=已有账号？点这登录").click()

    # get_by_text方法点击
    page.get_by_text("已有账号？点这登录").click()

    page.pause()