from playwright.async_api import async_playwright
from app.extractor.core import extract_fields

class PlaywrightEngine:
    def __init__(self, headless: bool = False):
        self.playwrite = None
        self.browser = None
        self.page = None
        self.headless = headless
    # start
    async def start(self):
        self.playwrite = await async_playwright().start()
        self.browser = await self.playwrite.chromium.launch(headless=self.headless)
        self.page = await self.browser.new_page()
    # navigate
    async def navigate(self, url) -> None:
        await self.page.goto(url)

        # await self.page.wait_for_timeout(5000)
        # html = await self.page.content()
        # with open("debug.html", "w", encoding="utf-8") as f:
        #     f.write(html)
    # click
    async def click(self, selector: str) -> None:
        await self.page.click(selector)
    # type
    async def type(self, selector: str, value) -> None:
        await self.page.fill(selector, value)
    # select
    async def select(self, selector: str, value: str) -> None:
        await self.page.select_option(selector, value)
    # wait for the value
    async def wait(self, wait_for: str | int) -> None:
        if isinstance(wait_for, int):
            await self.page.wait_for_timeout(wait_for)
        if isinstance(wait_for, str):
            await self.page.wait_for_selector(wait_for)

    async def extract(self, extract_map: dict) -> dict:
        return await extract_fields(self.page, extract_map)

    async def stop(self):
        await self.browser.close()
        await self.playwrite.stop()
