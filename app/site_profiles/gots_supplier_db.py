profile = {
    "id": "gots_supplier_db",
    "url": "https://global-standard.org/find-suppliers-shops-and-inputs/certified-suppliers/database/search",
    "fields": {
        "supplier_id": "#xFormForm-0-free_text",
        "product_category": "input[placeholder='Product category']",
        "field_of_operation": "input[placeholder='Field of operation']",
        "country": "input[placeholder='Country']"
    },
    "actions": [
        { "wait": 2000 },

        { "type": { "supplier_id": "VALUE" } },

        { "click": "product_category" },
        { "type": { "product_category": "VALUE" } },

        { "click": "field_of_operation" },
        { "type": { "field_of_operation": "VALUE" } },

        { "click": "country" },
        { "type": { "country": "VALUE" } },

        { "click": "button:has-text('Search Results')" },
        { "wait": "table.ui-table.search-result-list tr[class^='rowid']" }
    ],
    "extract": {
        "row_selector": "table.ui-table.search-result-list tr[class^='rowid']",
        "fields": {
            "company": "td.col-1",
            "country": "td.col-2",
            "categories": "td.col-3",
            "details_url": "td.col-5 a[href]"
        }
    }
}
