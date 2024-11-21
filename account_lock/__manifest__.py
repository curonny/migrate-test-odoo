{
    "name": "Irreversible Lock Date",
    "version": "15.0.1.0.0",
    "category": "Accounting/Accounting",
    "description": "\n    Make the lock date irreversible:\n\n    * You cannot set stricter restrictions on advisors than on users. Therefore, the All Users Lock Date must be anterior (or equal) to the Invoice/Bills Lock Date.\n    * You cannot lock a period that has not yet ended. Therefore, the All Users Lock Date must be anterior (or equal) to the last day of the previous month.\n    * Any new All Users Lock Date must be posterior (or equal) to the previous one.\n    ",
    "depends": [
        "account"
    ],
    "data": [],
    "license": "LGPL-3"
}