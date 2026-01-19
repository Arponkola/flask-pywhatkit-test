from flask import Blueprint, render_template, request, redirect, url_for
from app.model import BaseModel
from app.model.user_details import User
from app.routes.settings import DB_PATH


form_bp = Blueprint(
    "form_route", __name__,
    template_folder="templates",
    static_folder="static"
)

@form_bp.route("/form", methods=["GET", "POST"])
def form():
    if request.method=="POST":
        sender_mobile = request.form.get("SenderMobile")
        receiver_mobile = request.form.get("ReceiverMobile")
        scheduling_time = request.form.get("SchedulingTime")
        msg = request.form.get("Msg")
        count = request.form.get("Count")
        
        md = BaseModel(DB_PATH)
        db = md.create_db()
        
        user = User(db)
        status = user.insert_details(
            {
                "sender_mobile" : sender_mobile,
                "receiver_mobile": receiver_mobile,
                "scheduling_time" : scheduling_time,
                "msg" : msg,
                "count" : count
            }
        )
        if status:
            return "<h1> Your Response Is Submitted </h1>"
        return redirect(url_for("form_route.form"))
        
    return render_template("form.html")