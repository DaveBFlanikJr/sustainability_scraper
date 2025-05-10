from app.extractor.tables import extract_table_fields
from app.extractor.popups import extract_popup_fields

async def extract_fields(page, extract_map: dict) -> dict:
    results = {}

    if "fields" in extract_map:
        results.update(await extract_table_fields(page, extract_map["fields"]))

    if "popup_fields" in extract_map:
        results.update(await extract_popup_fields(page, extract_map["popup_fields"]))

    return results
