from  playwright.sync_api import sync_playwright
"""
1. css selector --简称css
#username id=username

2. xpath //*[@id="password"]

3. text 文本选择器 （非常实用），下面三种都可以用text定位 -- selenium没有

    3.1 <a href="超链接">文本</a>
    3.2 input里面的value值 <input class="btn btn-success btn-block disabled" id="loginBtn" type="submit" value="立即登录 > " disabled="disabled">
    3.3 <button >点击按钮</button> 中间的文本

4. 组合定位


常用的方法
fill 一次性的输入内容多个内容（类似复制粘贴）
type 一个个的输入（类似键盘输入）
click 点击按钮
clear 清空

查找元素的几种情况：
1. 如果一直找不到元素 （playwright._impl._api_types.TimeoutError: Timeout 30000ms exceeded.），超过30秒会超时
2. 找到一个元素
3. 找到多个元素
4. 等x秒才能找到一个或多个

click 动作的时候，找不到元素的时候会轮询从页面查找元素，30秒超时 （selenium此功能是需要封装的）

"""

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.108.155.10/login.html")

    # 定位元素 selector: str,
    # 第一种 page.locator(selector语法).fill("输入的内容")
    # page.locator("#username").fill("yoyo")

    # 第二种 page.fill("selector语法","输入的内容")
    # page.fill("#username","yoyo")
    # page.wait_for_timeout(3000)
    # page.locator("#username").clear() # 清除内容

    # xpath 语法定位密码框，locator会自动识别我们输入的是xpath还是css语法
    # page.locator('//*[@id="password"]').fill("aa123456")

    # 显式的语法（就是明确标识使用的是css和xpath）
    # page.fill("css=#username","yoyo")
    # 输入框父子组合定位
    page.fill("#login-form >> //*[@id='username']",'yoyo')
    page.wait_for_timeout(2000)
    page.locator('xpath=//*[@id="password"]').type("aa123456")

    # text 文本选择器定位 （模糊匹配），文本选择器需要指定text= css和xpath方式不需要因为它们都有其固定的标识
    # 模糊匹配的时候不能删除中间的内容如：没有这注册
    # 只能删除前后的内容如：没有账号？、点这注册
    # page.locator("text=没有账号？点这注册").click()
    # page.locator("text=没有账号？").click()
    # page.locator("text=点这注册").click()

    # text=""、text='' 像这两种，text后面的值加了双引号或单引号就是精确匹配
    # page.locator("text='立即登录'").click() #找不到的时候会轮询30秒，直到超时
    # page.locator("text='立即登录 > '").click()

    # 二次定位 父-->子孙 可以从1级父目录 >> 要定位的5级子目录，也可以找4级父目录，只要确保相关目录能定位到
    # css与text组合
    # page.locator("#login-div").locator("text=立即登录 > ").click()
    # page.locator("#login-div >> text=立即登录").click()
    # css与xpath组合
    # page.locator("#login-div").locator('//*[@id="loginBtn"]').click()
    # page.locator("#login-div >> //*[@id='loginBtn']").click()
    # xpath与text组合
    # page.locator('//*[@id="login-div"]').locator("text=立即登录 > ").click()
    page.locator('//*[@id="login-div"] >> text=立即登录').click()

    page.pause() # 断点