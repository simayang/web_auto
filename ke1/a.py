"""
"""

from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    # browser = p.chromium.launch(headless=False,channel="chrome") # 启动chromium 浏览器,默认是挂后台执行，需要前端显示出来的话headless=False
    # browser = p.firefox.launch(headless=False) # 打开火狐浏览器
    # browser = p.webkit.launch(headless=False) # 打开mac上的webkit浏览器
    browser = p.chromium.launch_persistent_context(user_data_dir=".\sima_chrome",headless=False)
    page = browser.new_page() # 打开一个标签页
    page.goto("https://www.baidu.com") # 打开百度地址
    print(page.title()) # 打印当前页title

    # 运行完成后会关闭浏览器，我们可以打个断点看下效果
    page.pause() # 断点

    # browser.close() # 关闭浏览器对象
