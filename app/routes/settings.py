import os

ADMIN = os.getenv("ADMIN_USER")
PASSWORD = os.getenv("ADMIN_PASS")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = "messege_db.db"
DB_PATH = os.path.join(BASE_DIR, "..", "instance", DB_NAME)