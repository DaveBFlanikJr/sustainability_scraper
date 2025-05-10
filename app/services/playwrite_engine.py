from playwright.async_api import async_playwright


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
        results = {}

        # Normal table results
        for key, selector in extract_map.get("fields", {}).items():
            try:
                await self.page.wait_for_selector(selector, timeout=15000)
                htmlelements = await self.page.query_selector_all(selector)
                if htmlelements:
                    text_list = []
                    for el in htmlelements:
                        text = await el.inner_text()
                        text_list.append(text.strip())

                    results[key] = text_list
                else:
                    results[key] = []
            except Exception:
                results[key] = []

        # Additional popup fields
       # Popup-specific fields (single values per key)
        popup_fields = extract_map.get("popup_fields", {})
        for key, selector in popup_fields.items():
            try:
                print(f"[extract:popup_fields] Trying to extract: {key} from selector: {selector}")
                await self.page.wait_for_selector(selector, timeout=5000)
                el = await self.page.query_selector(selector)
                text = await el.inner_text() if el else ""
                cleaned = text.split(":", 1)[-1].strip()
                results[key] = cleaned
            except Exception:
                results[key] = ""


        return results

    async def stop(self):
        await self.browser.close()
        await self.playwrite.stop()
