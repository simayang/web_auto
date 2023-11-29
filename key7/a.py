"""
日历控件，只有两种：
1、input标签中没有 readonly 属性的，能直接输入
2、input标签中有 readonly 属性的，不能直接输入
     解决思路：去掉 readonly 属性(JS 操作)，然后正常输入
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page()
    page.goto("http://47.116.12.183:8200/users/login/")

    # 先登录
    page.locator("#username").type("123@qq.com")
    page.locator("#password_l").fill("123456")
    page.locator("#jsLoginBtn").click()

    # 进入个人中心，输入日期
    page.goto("http://47.116.12.183:8200/users/userinfo/")
    # 输入日期，delay是延迟时间x秒（单位是毫秒）
    page.locator("#date_day").type("2023-11-21",delay=1000)

    # 去除readonly属性
        # 定义个变量接收js去除某元素的语法
    js1 = "document.getElementById('birth_day').removeAttribute('readonly')"
        # 使用evaluate去除该元素
    page.evaluate(js1)
    page.locator("#birth_day").type("2023-11-15", delay=100)
    # 断点
    page.pause()

