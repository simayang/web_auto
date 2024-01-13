"""
断言元素：
    1、元素是否可点击(是否是禁用状态)
    2、断言提示语
    3、断言输入框内容
"""

from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    # goto打开的页面，也可以networkidle (等页面加载完成后下一步)
    page.goto("http://47.116.12.183/login.html", wait_until="networkidle")

    # 点击登录按钮之前断言是否有提示语（应为false）
    text = page.locator('[data-fv-validator="notEmpty"][data-fv-for="username"]')
    print("看登录前提示语是否显示：",text.is_visible())
    print("打印提示语:{}".format(text.inner_text()))

    page.locator('text=立即登录').click()
    print("看登录按钮是否被禁用：",page.locator('text=立即登录').is_disabled())
    print("看登录按钮是否未被禁用：",page.locator('text=立即登录').is_editable())
    assert page.locator('text=立即登录').is_disabled()
    assert page.locator('text=立即登录').is_editable()==False
    # 断言按钮是否被禁用
    expect(page.locator('text=立即登录')).to_be_disabled()


    # 点击登录按钮之后断言是否有提示语（应为true）
    text2 = page.locator('[data-fv-validator="notEmpty"][data-fv-for="username"]')
    print("看登录后的提示语是否显示：",text2.is_visible())
    print("打印提示语:{}".format(text2.inner_text()))
    assert text2.is_visible()
    assert text2.inner_text() == "不能为空"

    expect(text2).to_be_visible()
    expect(text2).to_contain_text("不能为空")

    # 输入框--断言场景
    page.get_by_label("用 户 名").type("hello world")
    # .input_value()是输入框的内容获取
    print(page.get_by_label("用 户 名").input_value())
    assert page.get_by_label('用 户 名').input_value() == "hello world"

    expect(page.get_by_label("用 户 名")).to_have_value("hello world")

    # 清空输入框
    page.get_by_label('用 户 名').clear()
    expect(page.get_by_label('用 户 名')).not_to_have_value("hello world")

    page.pause()