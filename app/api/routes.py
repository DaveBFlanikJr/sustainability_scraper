from fastapi import APIRouter
from app.api.schema import CrawlRequest, CrawlResponse
from app.services.base_crawler import Crawler

router = APIRouter()

@router.post("/scrape", response_model=CrawlResponse)
async def scrape(req: CrawlRequest):
    crawler = Crawler(req)
    result = await crawler.run()
    return CrawlResponse(**result)
