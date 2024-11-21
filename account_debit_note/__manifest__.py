{
    "name": "Debit Notes",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "summary": "Debit Notes",
    "description": "\nIn a lot of countries, a debit note is used as an increase of the amounts of an existing invoice \nor in some specific cases to cancel a credit note. \nIt is like a regular invoice, but we need to keep track of the link with the original invoice.  \nThe wizard used is similar as the one for the credit note.\n    ",
    "depends": [
        "account"
    ],
    "data": [
        "wizard/account_debit_note_view.xml",
        "views/account_move_view.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3"
}