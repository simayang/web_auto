"""
滑块解锁，分为以下几步
1、获取滑动模块的位置
2、拿到滑动模块的 长和宽
3、定位到x和y的中间位置
4、按住，进行滑动（页面查看横向滑动多少px）
5、释放
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto(r"D:\test\hrun\web_auto_git\web_auto\key9\slider.html")

    # 获取坐标
    target = page.locator(".slider").bounding_box()
    print(target) # 打印获取到的坐标以及滑动模块的宽、高

    # 定位滑动模块中间，按住
    page.mouse.move(x=int(target['x'] + target['width']/2),y=int(target['y'] + target['height']/2))
    page.mouse.down()

    # 移动，先页面看看需要移动多少px
    page.mouse.move(x=int(target['x'] + target['width']/2 + 248),y=int(target['y'] + target['height']/2))

    # 释放
    page.mouse.up()

    page.pause()
