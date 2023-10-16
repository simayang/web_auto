"""
录制脚本 - 同步脚本
playwright codegen http://网站地址 （也可以不输入网站，直接回车后再输入）
"""

from playwright.sync_api import Playwright, sync_playwright,expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://124.70.221.221:8200/users/login/")
    page.get_by_placeholder("请输入您的邮箱地址").click()
    page.get_by_placeholder("请输入您的邮箱地址").fill("814834942@qq.com")
    page.get_by_placeholder("请输入您的密码").click()
    page.get_by_placeholder("请输入您的密码").fill("ai69662569")
    page.get_by_role("button", name="立即登录 >").click()

    # ---------------------
    page.wait_for_timeout(3000)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
