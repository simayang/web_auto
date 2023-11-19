"""
一闪而过的消息提示框，元素：
1、元素在dom 隐藏的，点击触发-显示
2、不在dom里面， 点击之后动态载入的 （这是本节元素特征）

定位的时候正常定位即可，用css、xpath等等，正常定位即可
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page()
    page.goto("http://localhost:63342/web_auto/yoyo/t.html")
    # 点击按钮
    page.locator('.btn.btn-info').click()

    # 定位一闪而过的消息
    # msg = page.locator(".toast-message")
    # print(f"判断元素是否显示：{msg.is_visible()}")
    # print(f"获取消息内容：{msg.inner_text()}")
    # import time
    # time.sleep(3)
    # print(f"判断元素是否显示：{msg.is_visible()}")

    # 断言一闪而过的消息
    # 第一种：元素本身就在页面上（隐藏状态），触发后，变成显示状态
    info  = page.get_by_text("info 消息提示")
    print(info.is_visible()) # 判断元素是否显示

    # 第二种：元素动态加载到页面
    info2 = page.locator(".toast-message")
    print(info2.inner_text()) # 获取元素的消息内容
    assert info2.inner_text() == "info 消息提示"