from services.playwright_engine import PlaywrightEngine
from app.api.schemas import CrawlRequest, CrawlResponse


class Crawler:
    def __init__(self, config: CrawlRequest):
        self.config = config
        self.engine = PlaywrightEngine()

    async def run(self) -> dict:
        try:
            await self.engine.start()
            await self.engine.navigate(self.config.url)

            # do each of the actions
            for action in self.config.actions:
                if action.click:
                    await self.engine.click(action.click)
                if action.type:
                    for selector, value in action.type.items():
                        await self.engine.type(selector,value)
                if action.select:
                    for selector, value in action.select.items():
                        await self.engine.select(selector,value)
                if action.wait:
                    await self.engine.wait(action.wait)

            data = await self.engine.extract(self.config.extract)
            await self.engine.stop()
            # return
            return {
                "success": True,
                "data": data,
                "error": None
            }

        except Exception as e:
            await self.engine.stop()
            return {
                "success": False,
                "data": {},
                "error": str(e)
            }
