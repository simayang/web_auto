
from playwright.sync_api import sync_playwright

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False,channel='chrome')

    # //ul/li/button/span[text()="确 定"]
    page = browser.new_page()
    page.goto("https://entry-test.eastbuy.com/")
    page.get_by_placeholder("请输入域账号").type("simayangyang")
    page.get_by_placeholder("请输入密码").type("123456")
    page.get_by_text("登  录").click()

    # 点击支付按钮
    page.get_by_text("支付").click()
    page.wait_for_timeout(2000)
    # 点击清分记录查询
    page.locator('//*[text()="清分记录查询"]').last.click()
    # 定位订单编号输入框，并输入内容
    page.locator('#orderId').type('372926890947728521')
    # 点击起始日期选择框
    # page.get_by_placeholder("起始日期").click()
    # page.get_by_title("2023-11-01").get_by_text("1").click()
    # page.get_by_role("button", name="确 定").click()
    # page.get_by_title("2023-11-15").get_by_text("15").click()
    # page.get_by_role("button", name="确 定").click()

    # 点击查询按钮
    # page.get_by_role('button',name='查 询').click()
    page.get_by_placeholder("起始日期").click()
    # 打断点
    page.pause()

    # page.locator('//ul/li/button/span[text()="确 定"]').click()
    # page.locator('[placeholder="结束日期"]').fill('2023-11-15 21:37:20')
    # page.locator('//ul/li/button/span[text()="确 定"]').click()

