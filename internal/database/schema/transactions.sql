CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    inventory_id INTEGER NOT NULL,
    count_purchased INTEGER NOT NULL,
    price_at_purchase REAL NOT NULL,
    paid BOOLEAN DEFAULT FALSE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(account_id) REFERENCES accounts(id),
    FOREIGN KEY(inventory_id) REFERENCES inventory(id)
);