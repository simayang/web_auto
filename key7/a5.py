"""
新增一个项目，并断言是否新增成功

1、先正常新增
2、获取当前项目名称列所以内容：.all
3、再判断我们新增的内容在不在返回的内容里面:many.all_inner_texts() 获取返回的内容并以文本形成呈现
"""

from playwright.sync_api import sync_playwright
import uuid
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 先登录
    page.locator("//*[@id='username']").type("sima")
    page.locator("//*[@id='password']").type("123456")
    page.locator('//*[@id="loginBtn"]').click()

    page.wait_for_timeout(3000) # 等3秒
    # 访问到项目列表
    page.goto("http://47.116.12.183/list_project.html")

    # 点击新增
    page.locator("#btn_add").click()
    # 定义个变量接收随机的项目名称 [:6]取出来前5个
    p_name = str(uuid.uuid4())[:6]
    # 填写项目名称
    page.locator("#addModal #project_name").fill(p_name)
    # 点击保存
    page.locator("#add_edit").click()
    page.wait_for_timeout(2000)
    # 获取当前项目名称列
    many = page.locator("//*[@id='table']/tbody//td[3]")
    print(many.all_inner_texts()) # 打印获取到的列表，all_inner_texts() 并以文本的形式打印

    assert p_name in many.all_inner_texts() # 断言新增的项目名称是否在获取到的列表中

    page.pause()