from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("http://124.70.221.221:8200/users/login/")
    page.get_by_placeholder("请输入您的邮箱地址").click()
    page.get_by_placeholder("请输入您的邮箱地址").fill("814834942@qq.com")
    page.get_by_placeholder("请输入您的密码").click()
    page.get_by_placeholder("请输入您的密码").fill("ai69662569")
    page.get_by_role("button", name="立即登录 >").click()
