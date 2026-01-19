import sqlite3 as sql
from typing import Dict

class BaseModel:
    def __init__(self, path:str):
        self.conn = sql.connect(path)
        self.conn.row_factory = sql.Row
        self.curr = self.conn.cursor()
    
    def create_db(self)->Dict:
        db = {
            "connection" : self.conn,
            "cursor" : self.curr
        }
        return db