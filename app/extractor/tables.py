

async def extract_table_fields(page, fields: dict) -> dict:
    table_results = {}
    for key, selector in fields.items():
        try:
            await page.wait_for_selector(selector, timeout=15000)
            elements = await page.query_selector_all(selector)
            table_results[key] = [ (await el.inner_text()).strip() for el in elements ] if elements else []
        except Exception:
            table_results[key] = []
    return table_results
