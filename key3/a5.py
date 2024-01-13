"""
定位百度中非下拉框的元素
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome',headless=False)
    page = browser.new_page() # 新开标签页
    page.goto("https://www.baidu.com/")
    page.locator('#s-usersetting-top').hover() # hover 鼠标悬停

    # 点击搜索设置-->高级搜索
    page.get_by_text("搜索设置").click()

    page.wait_for_timeout(1500)
    page.locator('.pfpanel-bd.c-font-normal [data-tabid="advanced"]').click()
    # page.locator('#adv-setting-gpc .c-icon.c-select-arrow').click()
    # page.locator('#adv-setting-gpc .c-select-dropdown-list>.c-select-item.c-select-item-selected').click()
    page.locator("#adv-setting-gpc").get_by_text("").click()
    page.get_by_text("一周内").click()
    page.pause()
    # 远程修改
    # 本地修改