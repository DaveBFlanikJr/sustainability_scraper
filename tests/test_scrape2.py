import httpx
import asyncio

async def run_test():
    payload = {
        "url": "https://global-standard.org/find-suppliers-shops-and-inputs/certified-suppliers/database/search",
        "actions": [
            { "wait": 2000 },

            # Free text field
            { "type": { "#xFormForm-0-free_text": "00159674" } },

            # # Product category
            # { "click": "input[placeholder='Product category']" },
            # { "type": { "input[placeholder='Product category']": "A" } },
            # { "wait": 1000 },
            # { "click": "ul.ui-autocomplete li:has-text('Accessories')" },

            # # Field of operation
            # { "click": "input[placeholder='Field of operation']" },
            # { "type": { "input[placeholder='Field of operation']": "M" } },
            # { "wait": 1000 },
            # { "click": "ul.ui-autocomplete li:has-text('Manufacturing')" },

            # # Country
            # { "click": "input[placeholder='Country']" },
            # { "type": { "input[placeholder='Country']": "Jap" } },
            # { "wait": 1000 },
            # { "click": "ul.ui-autocomplete li:has-text('Japan')" },

            # Submit
            { "click": "button:has-text('Search Results')" },
            { "wait": 5000 }
        ],
        "extract": {
            "results": "table.ui-table.search-result-list tr[class^='rowid']",
            "no_results": "#xFormText-0"
        }
    }




    async with httpx.AsyncClient(timeout=60.0) as client:  # timeout in seconds
        response = await client.post("http://localhost:3001/scrape", json=payload)
        print(response.json())

if __name__ == "__main__":
    asyncio.run(run_test())
