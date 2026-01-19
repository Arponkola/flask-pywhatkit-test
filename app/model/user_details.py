from typing import Dict, List
import sqlite3 as sql

class User:
    def __init__(self, db:Dict):
        self.connection = db["connection"]
        self.cursor = db["cursor"]
        self.table_name = "user_finding"
    
    def create_table(self, table_name:str):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                SENDER_MOBILE INTEGER PRIMARY KEY,
                RECEIVER_MOBILE INTEGER,
                SCHEDULING_TIME TIME,
                MSG TEXT,
                COUNT_TIMES INTEGER
                STATUS INTEGER DEFAULT 0
            )
        """)
        self.connection.commit()
    
    def insert_details(self, details:Dict)->bool:
        try:
            stime = str(details.get("scheduling_time"))
            self.cursor.execute(
                f"""
                    INSERT INTO user_finding VALUES(?, ?, ?, ?, ?, ?)
                """, (
                    details.get("sender_mobile"),
                    details.get("receiver_mobile"),
                    f'{stime}',
                    details.get("msg"),
                    details.get("count"),
                    0
                )
            )
            self.connection.commit()
            return True
        except Exception as e:
            print("Eroor Is  : ", e)
            return False
    
    def get_msg_by_time(self, current_time)->List:
        # 0 Means messege not sended
        # 1 Means messege sended
        details = self.cursor.execute(
            """
                SELECT * FROM user_finding WHERE STATUS=0 AND SCHEDULING_TIME=?
            """,(current_time,)
        ).fetchone()
        
        return details
    
    def mark_as_processed(self, mobile_number):
        self.cursor.execute(
            "DELETE FROM user_finding WHERE sender_mobile=?",
        (mobile_number, ))
        self.connection.commit()