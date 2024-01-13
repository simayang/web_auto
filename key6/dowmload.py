"""
文件下载
单个文件的下载 with的方法，会等待文件下载完毕后再关闭窗口（即便没有断点）

"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel='chrome')
    page = browser.new_page()
    page.goto("http://localhost:63342/web_auto/key6/download.html")

    # with page.expect_download() 会等待文件下载完成
    with page.expect_download() as dl:
        page.get_by_text('v113版本').click()
    download = dl.value
    path = download.path()
    print('获取下载的url地址：',download.url)
    # 下载下来，生成一个随机uuid保存
    print(download.path())
    # 用save_as 保存到本地
    download.save_as(download.suggested_filename)

    browser.close()
    # page.pause()