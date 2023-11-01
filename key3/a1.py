from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page() # browser.new_page 打开标签页
    page.goto("http://47.108.155.10/login.html") # page.goto 访问某网站

    page.locator("#username").fill("yoyo") # css语法根据ID 定位到用户名输入框，输入yoyo

    page.wait_for_timeout(2000) # 间隔2秒

    # page.locator("#username").fill("hello world") # css语法根据ID 再次定位到用户名输入框，输入hello world
    page.locator("#username").type("hello 你好！",delay=100)

    page.pause() # pause() 打个断点调试
    # 一个字符一个字符地输入字段，就好像它是一个使用locator.type()的真实键盘的用户
