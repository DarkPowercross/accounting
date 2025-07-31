CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT NOT NULL,
    account_address TEXT NOT NULL,
    account_telephone TEXT NOT NULL
);

CREATE TABLE accounts_contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    FOREIGN KEY(account_id) REFERENCES accounts(id)
);