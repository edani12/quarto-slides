
import sqlite3 
db_file = 'lecture17.db' 
conn = sqlite3.connect(db_file) 
cur = conn.cursor() 

# Find M names
cur.execute("SELECT * FROM drivers WHERE driver_name LIKE 'M%';")
print("--- Drivers starting with M ---")
for row in cur.fetchall(): print(row)

# Find 7 char nationalities
cur.execute("SELECT * FROM drivers WHERE LENGTH(nationality) = 7;")
print("\n--- Nationalities with 7 chars ---")
for row in cur.fetchall(): print(row)

# Find L or M names
cur.execute("SELECT * FROM drivers WHERE driver_name LIKE 'L%' OR driver_name LIKE 'M%';")
print("\n--- Drivers starting with L or M ---")
for row in cur.fetchall(): print(row)

# Find 1-10 wins
cur.execute("SELECT * FROM drivers WHERE victories BETWEEN 1 AND 10;")
print("\n--- Drivers with 1-10 wins ---")
for row in cur.fetchall(): print(row)

conn.close()