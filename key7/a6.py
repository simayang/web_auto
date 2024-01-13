"""
删除一个项目并断言是否删除的不在列表中
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 先登录
    page.locator("//*[@id='username']").type("test")
    page.locator("//*[@id='password']").type("123456")
    page.locator('//*[@id="loginBtn"]').click()

    page.wait_for_timeout(3000) # 等3秒
    # 访问到项目列表
    page.goto("http://47.116.12.183/list_project.html")

    # 根据文本属性定位某一列的元素
    name1 = "be0cf3"
    x1 = "//*[@id='table']/tbody/tr[1]/td[3]/a[text()='{}']/../../td[9]/a[2]".format(name1)
    page.locator(x1).click()
    page.locator("//*[text()='确定删除']").click()

    page.wait_for_timeout(2500)
    # 获取当前项目名称列
    many = page.locator("//*[@id='table']/tbody//td[3]")
    print(many.all_inner_texts()) # 打印获取到的列表，all_inner_texts() 并以文本的形式打印

    assert name1 not in many.all_inner_texts() # 断言删除的项目是否不在列表中

    page.pause()