{
    "name": "Check Printing Base",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "summary": "Check printing commons",
    "description": "\nThis module offers the basic functionalities to make payments by printing checks.\nIt must be used as a dependency for modules that provide country-specific check templates.\nThe check settings are located in the accounting journals configuration page.\n    ",
    "depends": [
        "account"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/account_check_printing_data.xml",
        "views/account_journal_views.xml",
        "views/account_move_views.xml",
        "views/account_payment_views.xml",
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "wizard/print_prenumbered_checks_views.xml"
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3"
}