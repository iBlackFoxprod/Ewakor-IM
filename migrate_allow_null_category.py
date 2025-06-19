import sqlite3

DB_PATH = 'instance/ewakor.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. Rename the old table
cursor.execute('ALTER TABLE products RENAME TO products_old;')

# 2. Create the new table with category nullable
cursor.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    product_type VARCHAR(50) NOT NULL,
    container_type VARCHAR(50),
    packaging VARCHAR(20) DEFAULT 'Unité',
    quantity INTEGER DEFAULT 0,
    unit_price FLOAT DEFAULT 0.0,
    image_path VARCHAR(200),
    min_stock_level INTEGER DEFAULT 10,
    unit VARCHAR(20) DEFAULT 'pcs',
    created_at DATETIME,
    updated_at DATETIME
);
''')

# 3. Copy data
cursor.execute('''
INSERT INTO products (id, name, description, category, product_type, container_type, packaging, quantity, unit_price, image_path, min_stock_level, unit, created_at, updated_at)
SELECT id, name, description, category, product_type, container_type, packaging, quantity, unit_price, image_path, min_stock_level, unit, created_at, updated_at FROM products_old;
''')

# 4. Drop the old table
cursor.execute('DROP TABLE products_old;')

conn.commit()
conn.close()
print('products.category is now nullable.') 