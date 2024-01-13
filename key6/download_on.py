"""
事件监听：
-  page.on(event )   全局事件监听,不管多少次都会监听
    - 如果使用 page.on("download", handler) 方式处理文件下载，会有个问题：由于代码运行太快，
    可能下载文件没下载完成，就直接关闭了上下文，保存到本地代码就会报错。
    所有需要等待他下载完成，下载时间我们无法控制，所以这种方式有缺陷。
-  page.once(event)   全局事件监听,只监听一次,只会触发一次下载事件
-  with page.expect_xx   点按钮触发的单个事件
- dispatch_event()  取消监听事件,没试成功

"""
from playwright.sync_api import sync_playwright

def handler_download(download):
    print(download.url) # 获取下载的地址
    print(download.suggested_filename) # 文件名称
    print(download.path()) # 则返回下载文件的路径。
    download.save_as(download.suggested_filename) # 保存到本地

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page()
    page.on('download',handler_download) # 全局监听
    page.goto("http://localhost:63342/web_auto/key6/download.html")


    # 触发第一个下载事件
    page.get_by_text('v113版本').click()
    # page.wait_for_timeout(10000)

    # 继续触发第二个下载事件
    page.get_by_text('v114版本').click()
    page.wait_for_timeout(10000)
    # browser.close()
