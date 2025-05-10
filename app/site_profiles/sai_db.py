# Profile for Social Accountability International
profile = {
    "id": "sai_db",
    "url": "https://sa-intl.org/sa8000-search/",
    "fields": {
        "org_name": "input.orgname",
        "cert_id": "input.certid",
        "cert_status": "input.certstatus",
        "cert_body": "input.certscope",
        "country": "input.country",
        "industry": "input.industry",
        "description": "input.description",
        "city": "input.city"
    },
    "actions": [
        { "wait": 2000 },

        { "type": { "org_name": "VALUE" } },
        { "type": { "cert_id": "VALUE" } },

        { "click": "cert_status" },
        { "type": { "cert_status": "VALUE" } },

        { "click": "cert_body" },
        { "type": { "cert_body": "VALUE" } },

        { "click": "country" },
        { "type": { "country": "VALUE" } },

        { "click": "industry" },
        { "type": { "industry": "VALUE" } },

        { "click": "description" },
        { "type": { "description": "VALUE" } },

        { "click": "city" },
        { "type": { "city": "VALUE" } },

        { "click": "button.search-btn[type='submit']" },
        { "wait": "table.ui-sortable-table tbody tr" },
        { "click": "table.ui-sortable-table tbody tr td a.ab-button" },
        { "wait": 5000 },
        { "wait": ".popup-overlay" },
        { "wait": ".popup-overlay .pop-content ul" }
    ],
    "extract": {
        "row_selector": "table.ui-sortable-table tbody tr",
        "fields": {
            "organization": "td:nth-child(1)",
            "certification_body": "td:nth-child(2)",
            "certificate_id": "td:nth-child(3)",
            "status": "td:nth-child(4)",
            "industry": "td:nth-child(5)",
            "workers": "td:nth-child(6)",
            "more_info_link": "td:nth-child(7) a"
        },
        "popup_fields": {
            "organization": ".popup-overlay .pop-content ul li:nth-child(1)",
            "certification_body": ".popup-overlay .pop-content ul li:nth-child(2)",
            "certificate_id": ".popup-overlay .pop-content ul li:nth-child(3)",
            "status": ".popup-overlay .pop-content ul li:nth-child(4)",
            "industry": ".popup-overlay .pop-content ul li:nth-child(5)",
            "address": ".popup-overlay .pop-content ul li:nth-child(6)",
            "initial_cert_date": ".popup-overlay .pop-content ul li:nth-child(7)",
            "latest_cert_date": ".popup-overlay .pop-content ul li:nth-child(8)",
            "expiration_date": ".popup-overlay .pop-content ul li:nth-child(9)"
        }
    }
}
