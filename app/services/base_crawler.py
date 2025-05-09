from app.services.playwrite_engine import PlaywrightEngine
from app.api.schema import CrawlRequest
from app.utils.loader import loader
from app.utils.action_filler import build_actions


class Crawler:
    def __init__(self, config: CrawlRequest):
        self.config = config
        self.engine = PlaywrightEngine()

        # check and see if we are our site_profile
        if config.site_id:
            self.profile = loader(config.site_id)
            self.url = self.profile["url"]
            self.actions = build_actions(self.profile, config.inputs or {})
            self.extract = { "results": self.profile["extract"]["row_selector"] }
        else:
            self.url = config.url
            self.actions = config.actions
            self.extract = config.extract

    async def run(self) -> dict:
        try:
            await self.engine.start()
            await self.engine.navigate(self.url)

            # do each of the actions
            for action in self.actions:
                if action.get("click"):
                    await self.engine.click(action["click"])
                if action.get("type"):
                    for selector, value in action["type"].items():
                        await self.engine.type(selector,value)
                if action.get("select"):
                    for selector, value in action["select"].items():
                        await self.engine.select(selector,value)
                if action.get("wait"):
                    await self.engine.wait(action["wait"])

            data = await self.engine.extract(self.extract)
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
