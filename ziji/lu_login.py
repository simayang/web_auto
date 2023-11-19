from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://entry-test.eastbuy.com/")
    page.goto("https://entry-test.eastbuy.com/index?redirect=")
    page.get_by_placeholder("请输入域账号").click()
    page.get_by_placeholder("请输入域账号").fill("simayangyang")
    page.get_by_placeholder("请输入域账号").press("Tab")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_text("登 录").click()
    page.get_by_text("清分记录查询").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
