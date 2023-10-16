"""
回顾之前学过的内容
    1. page.locator(selector:str)
    - xpath 语法： //*[@id='xx']  （不声明的）， xpath=//*[@id='xx'] （声明的）
    - css语法：#id.class_name （不声明的），css=#id （声明的）
    - text语法：也是基于xpath的， text=文本，什么情况下适用：
        - <a id="x" name="xx">a标签中间的文本</a>
        - <input type="button" value="button里的value文本值"
    - 组合语法：以上三种均可任意组合
        - //*[@id="xx"] >> #id
        page.locator("#login-form").locator("text=立即登录")

    2. 内置定位器
    • page.get_by_text() 通过文本内容定位。
    • page.get_by_label() 通过关联标签的文本定位表单控件。
    • page.get_by_placeholder() 按占位符定位输入。
    • page.get_by_title() 通过标题属性定位元素。
    • page.get_by_role() 通过显式和隐式可访问性属性进行定位。
    • page.get_by_alt_text() 通过替代文本定位元素，通常是图像。
    • page.get_by_test_id() 根据 data-testid 属性定位元素（可以配置其他属性）。

本节课： 主要是自己写
    1. html 元素认识
        - DOM document的缩写，什么是DOM呢，简单说就是打开网站后在html标签里的都是DOM，不是html标签里的比如浏览器本身的功能就不是DOM
        - 元素节点
            html 是根节点
                head 只需要关注title标签
                body 里面要看下层级结构
            层级关系 -- 也叫节点关系， 分为：父子层级、兄弟层级、子孙层级

    2. xpath
    - 单个元素的定位
        属性
        标签 * 所有标签
        @id   @name  @type  @class （class 最特殊 有空格，有多重属性）
        and 同时满足多个条件

    - 层级元素的定位
        -- 直接的父子关系
            $x("//form/button[@class='btn btn-success']")
            //父元素/子元素[@属性=属性值]，对应的是：//*标签/*子标签[@属性=属性值]

        -- 子孙关系
            子孙元素提取，语句为：$x("//div[@class='bs-bars pull-left']/form/button[@id='btn_add']")
            子孙元素提取，语法为：//父元素[@属性=父元素属性值]/子元素[@属性=子元素属性值]/孙元素[@属性=孙元素属性值]

    -- 多个子元素时
            可以通过下标，xpath下标是从1开始
            


    3. css
"""