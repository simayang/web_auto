"""
select内容定位

select_option("可见的选项")
 select_option(index=1)
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome',headless=False)
    page = browser.new_page() # 新开标签页
    page.goto("http://172.19.31.91:8000/api/login/")

    # 定位用户名和密码输入框，点击登录
    page.locator('#account').type("simayy")
    page.locator('#password').type("simayangyang@123")
    page.locator("#login_submit").click()

    # 点击项目列表
    page.get_by_text("项目管理").hover()
    page.get_by_text("项 目 列 表").click()

    # 定位select下拉框，先在控制台看一下语法对不对
    page.select_option("#pro_filter [name='project']","司马-示例")
    # 远程
    # 本地1
    page.pause()






