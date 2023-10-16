"""
查找元素的几种情况：
1. 如果一直找不到元素 （playwright._impl._api_types.TimeoutError: Timeout 30000ms exceeded.），超过30秒会超时
2. 找到一个元素 可以进行你的操作，click,fill
3. 找到多个元素 会报错，然后提示有多少个
4. 等x秒才能找到一个或多个
"""
"""
查找元素的几种情况：
1. 如果一直找不到元素 （playwright._impl._api_types.TimeoutError: Timeout 30000ms exceeded.），超过30秒会超时
2. 找到一个元素 可以进行你的操作，click,fill
3. 找到多个元素 会报错，然后提示有多少个
4. 等x秒才能找到一个或多个
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com/")
    # 角色定位
    # page.get_by_role("link", name="hao123").click()
    # first 多个时取第一个
    # page.locator("#s-top-left>.mnav").first.click()
    # last 多个时取最后一个
    # page.locator("#s-top-left>.mnav").last.click()
    # 取中间或者某一个，也可以nth(下标值)根据下标取值
    # page.locator("#s-top-left>.mnav").nth(2).click()
    print("数量有：",page.locator("#s-top-left>.mnav").count())
    all = page.locator("#s-top-left>.mnav").all() # 拿到所有的元素

    # 打印全部
    # a = [i.click() for i in all]

    # 打印部分
    a = [i for i in all]
    for j in range(3):
        a[j].click()
    page.pause()


# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.baidu.com/")
#     # 角色定位
#     # page.get_by_role("link", name="hao123").click()
#     # first 多个时取第一个
#     # page.locator("#s-top-left>.mnav").first.click()
#     # last 多个时取最后一个
#     # page.locator("#s-top-left>.mnav").last.click()
#     # 取中间或者某一个，也可以nth(下标值)根据下标取值
#     # page.locator("#s-top-left>.mnav").nth(2).click()
#     print("数量有：",page.locator("#s-top-left>.mnav").count())
#     all = page.locator("#s-top-left>.mnav").all() # 拿到所有的元素
#
#     # 打印全部
#     # a = [i.click() for i in all]
#
#     # 打印部分
#     a = [i for i in all]
#     for j in range(3):
#         a[j].click()
#     page.pause()

