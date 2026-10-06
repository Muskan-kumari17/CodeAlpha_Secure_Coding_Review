import sqlite3
import hashlib

username = input("Enter username: ").strip()
password = input("Enter password: ")

if not username or not password:
    print("Username and password are required.")
    exit()

password_hash = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = """
SELECT * FROM users
WHERE username = ? AND password = ?
"""

cursor.execute(query, (username, password_hash))

result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()