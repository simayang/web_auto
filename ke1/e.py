"""
录制脚本 - 异步
"""
import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://124.70.221.221:8200/users/login/")
    await page.get_by_placeholder("请输入您的邮箱地址").click()
    await page.get_by_placeholder("请输入您的邮箱地址").fill("814834942@qq.com")
    await page.get_by_placeholder("请输入您的密码").click()
    await page.get_by_placeholder("请输入您的密码").fill("ai69662569")
    await page.get_by_role("button", name="立即登录 >").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())