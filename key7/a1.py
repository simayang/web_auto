"""
table 表格定位
- table   thead/tbody
- tr  td/th

定位方式1：根据行和列 （tr[m]/td[n])
    $x('//*[@id="table"]/tbody/tr[1]/td[3]')

定位方式2： 根据指定列的指定名称（不管哪一行，通过列定位）
    解决思路：分2次
    - 第一次定位全部列
    - 第二次根据文本筛选
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 先登录
    page.locator("//*[@id='username']").type("sima")
    page.locator("//*[@id='password']").type("123456")
    page.locator('//*[@id="loginBtn"]').click()

    page.wait_for_timeout(3500) # 等待3.5秒

    # 再到项目列表定位表格元素
    # 第一种方法：通过行，定位列
    page.goto("http://47.116.12.183/list_project.html")
    page.locator("//*[@id='table']/tbody/tr[1]/td[3]/a").click()
    page.locator('#myModal .close>span').click()
    page.wait_for_timeout(2000)
    # 第二种方法：不管哪一行，直接定位列，然后再定位列上面的元素
    page.locator("//*[@id='table']/tbody/tr/td[3]").get_by_text("测试").click()

    page.pause()# 打断点

    # 本地mian