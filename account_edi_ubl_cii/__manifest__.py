{
    "name": "Import/Export electronic invoices with UBL/CII",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "description": "\nElectronic invoicing module\n===========================\n\nAllows to export and import formats: E-FFF, UBL Bis 3, EHF3, Factur-X (CII), XRechnung (UBL).\nWhen generating the PDF on the invoice, the PDF will be embedded inside the xml for all UBL formats. This allows the\nreceiver to retrieve the PDF with only the xml file. Note that **EHF3 is fully implemented by UBL Bis 3** (`reference \n<https://anskaffelser.dev/postaward/g3/spec/current/billing-3.0/norway/#_implementation>`_).\n\nThe formats can be chosen from the journal (Journal > Advanced Settings) linked to the invoice. \n\nNote that E-FFF and XRechnung (UBL) are only available for Belgian and German companies, \nrespectively. UBL Bis 3 is only available for companies which country is present in the `EAS list \n<https://docs.peppol.eu/poacc/billing/3.0/codelist/eas/>`_.\n\nNote also that you need to activate PDF A in order to be able to submit a Factur-X pdf on Chorus Pro: \ngo to Settings > Technical (debug mode) > System Parameters > select/create one with Key: edi.use_pdfa, Value: True. \nWith this setting, Chorus Pro will automatically detect the \"PDF/A-3 (Factur-X)\" format.\n    ",
    "depends": [
        "account_edi"
    ],
    "data": [
        "data/account_edi_data.xml",
        "data/cii_22_templates.xml",
        "data/ubl_20_templates.xml",
        "data/ubl_21_templates.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3"
}