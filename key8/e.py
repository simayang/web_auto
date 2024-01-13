"""
导航生命周期（默认load，通常用于 <body> 元素，在页面完全载入后(包括图片、css文件等等。)执行脚本代码。）：
wait_until:Union[“commit”，“domcontentloaded”，“load”，“networkidle”，None]当认为操作成
功时，默认为“加载”。事件可以是：
• commit：考虑在接收到网络响应并且文档开始加载时完成操作。
• domcontentloaded： 在触发“domcontentloaded”事件时完成操作。
• load： 触发 load事件时完成操作。
• networkidle： 当 500 毫秒内没有新的网络请求时触发，认为操作已完成。
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("http://47.116.12.183/login.html")
     # 先登录
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_text("立即登录").click()

    # 自动等待页面加载完成
    page.wait_for_load_state("networkidle")

    # 打印当前页面网页
    print(page.title())
    print(page.url)

    page.pause()