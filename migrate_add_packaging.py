import sqlite3

DB_PATH = 'instance/ewakor.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Check if the column already exists
cursor.execute("PRAGMA table_info(products);")
columns = [col[1] for col in cursor.fetchall()]

if 'packaging' not in columns:
    try:
        cursor.execute('ALTER TABLE products ADD COLUMN packaging VARCHAR(20) DEFAULT "Unité";')
        print("Column 'packaging' added.")
    except Exception as e:
        print(f"Error adding column: {e}")
else:
    print("Column 'packaging' already exists.")

conn.commit()
conn.close() 