{
    "name": "Proxy features for account_edi",
    "description": "\nThis module adds generic features to register an Odoo DB on the proxy responsible for receiving data (via requests from web-services).\n- An edi_proxy_user has a unique identification on a specific format (for example, the vat for Peppol) which\nallows to identify him when receiving a document addressed to him. It is linked to a specific company on a specific\nOdoo database.\n- Encryption features allows to decrypt all the user's data when receiving it from the proxy.\n- Authentication offers an additionnal level of security to avoid impersonification, in case someone gains to the user's database.\n    ",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "depends": [
        "account_edi"
    ],
    "external_dependencies": {
        "python": [
            "cryptography"
        ]
    },
    "data": [
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
    "post_init_hook": "_create_demo_config_param"
}