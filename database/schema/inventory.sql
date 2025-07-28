CREATE TABLE inventory_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    supplier_id INTEGER NOT NULL,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_type_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(inventory_type_id) REFERENCES inventory_type(id)
);

CREATE TABLE inventory_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    price REAL NOT NULL,
    effective_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(inventory_id) REFERENCES inventory(id)
);
