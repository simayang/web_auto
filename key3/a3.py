"""
聚焦元素，什么时候用到聚焦元素，当一个页面有下拉侧边栏的时候，下面的元素你不下拉是点击不到的
这时候用到聚焦元素

 locator.focus() 聚焦给定元素
"""

from  playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome',headless=False) # 定义变量接收 页面模式打开谷歌
    page = browser.new_page() # 打开标签页
    page.goto("https://www.baidu.com/")
    page.locator("#kw").type("上海悠悠博客")
    page.click("#su")

    page.wait_for_timeout(3000)

    page.get_by_role("link", name="上海-悠悠 - 博客园", exact=True).click()
    page.pause()
