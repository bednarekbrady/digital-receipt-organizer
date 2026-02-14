DROP TABLE IF EXISTS receipts;

CREATE TABLE receipts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    file_path TEXT NOT NULL
);