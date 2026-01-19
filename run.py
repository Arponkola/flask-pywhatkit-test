from app import create_app
from flask import render_template
from app.model import BaseModel
from app.model.user_details import User
import threading
import datetime
import time
import os
import pywhatkit
from app.routes.settings import DB_PATH

myapp = create_app()

def message_sender():
    bm = BaseModel(DB_PATH)
    db = bm.create_db()
    user = User(db)
    while True:
        now = datetime.datetime.now()
        current_time_str = now.strftime("%H:%M")
        user_data = user.get_msg_by_time(current_time_str)
        if user_data:
            try:
                print(user_data)
                phone = user_data["receiver_mobile"]
                message = user_data["msg"]
                curr_hour = now.hour
                curr_min = now.minute + 2
                
                print(f"Attempting to send to {phone}")
                pywhatkit.sendwhatmsg("+91"+str(phone), message, curr_hour, curr_min, 15, tab_close=True)
                print(f"Success: Message sent to {phone}")
                user.mark_as_processed(user_data['sender_mobile'])
            
            except Exception as e:
                print(f"Error sending to {user_data['receiver_mobile']}: {e}")
            
                
        time.sleep(60)


if __name__=='__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN"):
        background_thread = threading.Thread(target=message_sender, daemon=True)
        background_thread.start()
    myapp.run(debug=True)