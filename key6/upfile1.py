"""
文件上传：
.set_input_file 前面是定位上传的定位语句
1、单个文件上传：.set_input_file('文件名称或绝对路径')
2、多个文件上传：.set_input_files(['file1.txt', 'file2.txt'])

-- 自己调试的时候最好把同目录下放上要上传的文件，这样用相对路径即可

事件监听：
自动监听 标桩 input 控件才会生效 <input type="file" name="file" id="file">

非input：前面的.set_input_file （不生效）
    with page.expect_file_chooser() as fc:
        page.get_by_label("选择文件").click() # 定位点击选择文件按钮
    file_chooser = fc.value # 获取fc的value值
    file_chooser.set_files("1.jpg") # 然后再上传文件

palywright 不支持：上传整个文件夹

"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    # 打开新标签页
    page = browser.new_page()
    page.goto("http://localhost:63342/web_auto/key6/upfile.html")

    # 定位元素 -- label 的元素属性值和input的id属性值一致的时候，用label标签定位（中文更直观）
    # 仅限于input标签 -- 方式1
    page.get_by_label("选择文件").set_input_files("1.jpg")
    page.wait_for_timeout(2000)
    # 等两秒删除选择的内容
    page.get_by_label("选择文件").set_input_files([])




    # 通用的，不管是不是input标签 -- 方式二
    # with page.expect_file_chooser() as fc:
    #     page.get_by_label("选择文件").click()
    # file_chooser = fc.value
    # file_chooser.set_files("1.jpg")
    # print("返回与此文件选择器关联的输入元素：",file_chooser.element) # 返回与此文件选择器关联的输入元素
    # print("返回此文件选择器是否接受多个文件:",file_chooser.is_multiple) # 返回此文件选择器是否接受多个文件
    # print("返回此文件选择器所属的页面:",file_chooser.page) # 返回此文件选择器所属的页面
    # page.wait_for_timeout(2000)
    # file_chooser.set_files([])


    # # 事件监听 page.on("filechooser", ) 会自动监听filechooser 事件，只要有点击了选择文件按钮，就会自动触发
    # page.on('filechooser',lambda  filechooser: filechooser.set_files("1.jpg"))
    # # 点击选择文件按钮，会触发 filechooser 事件
    # page.get_by_label("选择文件").click()
    #
    # page.wait_for_timeout(3000)
    # # 等3秒后，再监听到选择事件时清空选择的内容
    # page.on("filechooser", lambda file_chooser: file_chooser.set_files([]))
    # page.get_by_label("选择文件").click()

    # # 打个断点
    page.pause()
