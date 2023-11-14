"""
126邮箱定位
    1.定位 iframe （有两个重要的属性：name或id（为啥是或就是有id用id没有id用name），以及url）


get_by_placeholder：定位placeholder属性的值
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page() # 打开新标签页
    page.goto("https://www.126.com/")

    # 定位账号输入内容
    print('打印所有的iframe：',page.frames)
    print('打印最外层iframe：',page.main_frame)
    frame = page.frame_locator("iframe[id^=x-URS-iframe]") # 进入到iframe

    frame.get_by_placeholder("邮箱账号或手机号码").type("123@qq.com") # 定位用户名输入框，输入内容
    frame.locator('[name="password"]').fill("123456") # 定位密码框，输入内容
    frame.locator("#dologin").click() # 定位登录按钮，输入内容

    page.pause()