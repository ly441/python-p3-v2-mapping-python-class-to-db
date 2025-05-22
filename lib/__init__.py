
# lib/__init__.py
import sqlite3
import os

# Connect to the database in the lib directory
DB_PATH = os.path.join(os.path.dirname(__file__), 'company.db')
CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()