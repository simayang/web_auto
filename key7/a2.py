"""
日历控件2种场景：
1. 输入框能输入， input  直接输入日期 + 时间
2. readonly 属性（仅仅可读，不能写）
  解决思路：去掉 readonly 属性(JS 操作)，然后正常输入
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.116.12.183:8200/users/login/")
    # 先登录
    page.get_by_placeholder("请输入您的邮箱地址").fill("123@qq.com")
    page.get_by_placeholder("请输入您的密码").fill("123456")
    page.get_by_text("立即登录").click()
    page.wait_for_timeout(5000)

    # 进入个人中心
    page.goto("http://47.116.12.183:8200/users/userinfo/")
    # 输入日期
    page.locator('#date_day').type("2023-11-15", delay=100)
    # 模拟在console 里面执行JavaScript
    js1 = 'document.getElementById("birth_day").removeAttribute("readonly");'
    js2 = 'document.getElementById("birth_day").value="2023-11-19";'
    page.evaluate(js1)
    page.evaluate(js2)

    page.pause()