{
    "name": "Import/Export Invoices From XML/PDF",
    "description": "\nElectronic Data Interchange\n=======================================\nEDI is the electronic interchange of business information using a standardized format.\n\nThis is the base module for import and export of invoices in various EDI formats, and the\nthe transmission of said documents to various parties involved in the exchange (other company,\ngovernements, etc.)\n    ",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "depends": [
        "account"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/account_invoice_send_views.xml",
        "views/account_edi_document_views.xml",
        "views/account_move_views.xml",
        "views/account_payment_views.xml",
        "views/account_journal_views.xml",
        "data/cron.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": True,
    "license": "LGPL-3"
}