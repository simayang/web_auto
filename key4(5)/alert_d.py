"""
1. 先要学会识别：alert、confirm、prompt
2. playwright 会默认关闭弹窗
3. 我们怎么知道成功弹出了呢？ -->事件的监听

"""
from playwright.sync_api import sync_playwright
import time

def handle_dialog1(dialog):
    """监听后处理"""
    print(dialog.message)
    if dialog.type == "alert":
        # assert  dialog.message == "您认识司马洋洋吗？"
        print("alert----------")
        time.sleep(3)
        dialog.dismiss() # 取消弹窗，会关闭弹窗

def handle_dialog2(dialog):
    """监听后处理"""
    print(dialog.message)
    if dialog.type == "confirm":
        # assert  dialog.message == "您认识司马洋洋吗？"
        print("confirm----------")
        time.sleep(3)
        dialog.dismiss() # 取消弹窗，会关闭弹窗

def handle_dialog3(dialog):
    """监听后处理"""
    print(dialog.message)
    if dialog.type == "prompt":
        # assert  dialog.message == "您认识司马洋洋吗？"
        print("prompt----------")
        dialog.accept(prompt_text='hello world')
        time.sleep(1)
    else:
        time.sleep(3)
        dialog.dismiss() # 取消弹窗，会关闭弹窗

    """
    侦听器必须dialog.accept()或dialog.dismiss()对话框 - 否则页面将冻结等待对话框，并且单击等操作将永远不会完成。
    函数中也可以写等待时间之类的

    监听是异步的，这个是selenium做不到的
    """

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,channel="chrome")
    page = browser.new_page()
    page.goto("http://localhost:63342/yoyo_web1/web_auto1-6/ke5/alert.html")

    # 加上下面这一句之后会显示弹窗内容
    # page.on("dialog",lambda  dialog:dialog.accept()) # 事件监听要在点击之前，注意:当没有page.on("dialog")侦听器存在时，所有对话框都会自动关闭。

    # page.on("dialog",lambda  dialog:print(dialog.message)) # 也可以打印监听的内容，但是lambda的话只能执行一件事情，
    # 如果想做多件事情我们就写成普通的函数即可， page.on("dialog",handle_dialog)
    page.on("dialog",handle_dialog1) # 这样一个监听动作就可以处理后续多个内容
    page.on("dialog",handle_dialog2)
    page.on("dialog",handle_dialog3)
    page.locator('#alert').click() # 点击的时候我们看不到打开后的效果，这是因为playwright会默认关闭弹窗（防止影响后续操作）
    page.locator("#confirm").click()

    # page.once 只监听一次
    # page.once('dialog', handler1)

    # 取消监听
    page.remove_listener("dialog",handle_dialog1) # 移除第一个监听内容

    # prompt
    page.locator('#prompt').click()

    page.pause() # 打个断点