# -*- coding: utf-8 -*-

{
    "name": "Landed Costs for Avarage Costing Method",
    "version": "11.0.1.0.0",
    "author": "Vauxoo,ATRIVIA",
    "category": "Generic Modules/Account",
    "website": "http://www.vauxoo.com/",
    "license": "AGPL-3",
    "depends": [
        "stock_landed_costs",
        "stock_deviation_account",
        "mrp",
        "stock_card",
    ],
    "demo": [
        # "demo/account_invoice_demo.xml",
    ],
    "data": [
        "views/stock_landed_costs.xml",
        "views/account_invoice.xml",
    ],
    "installable": True,
    "auto_install": False,
}
