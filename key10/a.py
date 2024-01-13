"""
页面断言
to_have_title() 确保页面具有给定的标题
not_to_have_title 与expect(page).to_have_title()相反
to_have_url 确保页面导航到给定的 URL
not_to_have_url 与expect(page).to_have_url()相反

使用示例：
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")
    title = page.title()
    print(title)
    print(page.url)
    expect(page).to_have_title("百度一下，你就知道")
    expect(page).to_have_url("https://www.baidu.com/")
与传统断言相比，传统断言比较死板只断言一次就确定是否成功且没有时间限制，虽然可以加等待时间但是如果元素早于
等待时间很多返回就浪费了很多时间
"""
from playwright.sync_api import sync_playwright,expect
import re
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("http://47.116.12.183/login.html", wait_until="networkidle")

    # 点去注册
    # page.get_by_text("没有账号？点这注册").click()

    # 传统断言
    # page.wait_for_timeout(2000)
    # print(page.title())
    # print(page.url)
    # assert page.title() == '注册'
    # assert '/register.html' in page.url

    #  page.expect_navigation() 显示断言, 显示断言重定向
    with page.expect_navigation(url='.*/register.html', timeout=2000):
        page.locator('text=没有账号？点这注册').click()
    print("1111111111111111111")

    # 默认时间是5秒，在5秒内会不断断言，超过5秒还是失败就为断言失败
    expect(page).to_have_title('注册',timeout=10000)
    expect(page).to_have_url(re.compile(".*/register.html"), timeout=10000)
    page.pause()

    # 与上面相反的断言，当前页面不包含该title和url
    expect(page).not_to_have_title("登录", timeout=5000)
    expect(page).not_to_have_url(re.compile(".*/login.html"), timeout=10000)















