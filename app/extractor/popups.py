async def extract_popup_fields(page, popups: dict) -> dict:
    popup_results = {}
    for key, selector in popups.items():
        try:
            await page.wait_for_selector(selector, timeout=5000)
            el = await page.query_selector(selector)
            text = await el.inner_text() if el else ""
            popup_results[key] = text.split(":", 1)[-1].strip()
        except Exception:
            popup_results[key] = ""
    return popup_results
