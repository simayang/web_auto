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
            //父元素/子元素[index]
    （不能从查找结果去index）
    - 文本查找
        //*[text()="文本内容"]

    - 包含  contains()
      id=sdd12333
      text()="sssssssssssssssssssssqwqq"

      $x('//*[contains(@id, "right-t")]') 是@id、name、type等内容，左边是属性，右边是包含的属性值
      $x('//*[contains(text(), "导出项目")]') 是text文本内容，左边是text()文本标签，右边是包含的文本内容

   - 面试 （子元素  找 父元素）   /..
     子元素/..

    3. css
    - 简写基本语法
        标签（类似 input from这些标签）、 #号=id、 .点=class (class 最特殊   有空格)  .class1.class2
        空格举例：$(".bs-bars pull-left) 需要写为$(".bs-bars.pull-left")

    - 通用的属性语法 [name="xx"]

    - 多个条件匹配
        input#id.class[name="xx"][type="text"]
        多个条件时，可以和上面的基本语法、通用属性任意组合定位

    - 层级关系
        父子关系   父 > 子
        子孙    父  子孙

    - 父 找 子 索引
    - 正则匹配
        $('[name^="value"]') 匹配 name 以 value 开头的元素
        $('[name$="end"]') 匹配 name 以 end 结尾的元素
        $('[class*="text"]') 匹配class属性包含text的元素

    操作元素
    - 点击   click() dblclick()
       检测（30 轮询查找)
       1. 显示还是隐藏    等待
       2. 遮挡
       3. 不在当前屏幕  聚焦
       4. 暂时没出现   等待
       5. 是否可点击

    - 输入   fill()      输入框直接赋值文本，相当于复制粘贴
        type()    模拟键盘的输入
    - 鼠标悬停 hover()
    - 聚焦元素  focus()  点击的时候自动处理


场景：
  select  (哪些是，哪些不是）
   option

 select_option("可见的选项")
 select_option(index=1)
"""