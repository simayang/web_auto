"""
异步运行 start() 和stop() 的方式
"""

from playwright.sync_api import  sync_playwright
p = sync_playwright().start() # 启动

browser = p.chromium.launch(headless=False) # headless = False 关闭非GUI模式
page = browser.new_page()
page.goto("https://www.baidu.com/")

browser.close() # 关闭浏览器对象
p.stop() # 停止