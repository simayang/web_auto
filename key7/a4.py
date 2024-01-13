"""
定位操作栏上面的X删除按钮

1、根据行和列：
    1.1、先定位到操作栏： //*[@id='table']/tbody/tr[1]/td[9]/a[2]
    1.2、再定位到取消删除按钮： $x("//*[text()='取消操作']")
2、根据项目名称定位删除按钮
    2.1、先定位到项目名称：//*[@id='table']/tbody/tr[1]/td[3]/a[text()='demo']
    2.2、再返回到同一行的位置：//*[@id='table']/tbody/tr[1]/td[3]/a[text()='demo']/../..
    2.3、然后拿到该行下面的第几列的某个按钮：//*[@id='table']/tbody/tr[1]/td[3]/a[text()='demo']/../../td[9]/a[2]
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("http://47.116.12.183/login.html")

    # 先登录
    page.locator("//*[@id='username']").type("sima")
    page.locator("//*[@id='password']").type("123456")
    page.locator('//*[@id="loginBtn"]').click()

    page.wait_for_timeout(3000) # 等3秒
    # 访问到项目列表
    page.goto("http://47.116.12.183/list_project.html")
    # 再控制台调试后点击操作栏删除按钮 -- 根据行和列
    # page.locator("//*[@id='table']/tbody/tr[1]/td[9]/a[2]").click()
    # page.locator("//*[text()='取消操作']").click() # 定位删除按钮
    # page.pause()

    # 根据文本属性定位某一列的元素
    name1 = "demo"
    x1 = "//*[@id='table']/tbody/tr[1]/td[3]/a[text()='{}']/../../td[9]/a[2]".format(name1)
    page.locator(x1).click()

    page.pause()