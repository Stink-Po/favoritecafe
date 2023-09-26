from app.public_views import *
from app.methods.sub_manager import SubManager
from flask import request, session


@app.route("/subs", methods=["GET", "POST"])
def sub():
    submitted_token = request.form.get('_csrf_token')
    stored_token = session.get('_csrf_token')
    
    if request.method == "POST":
        if submitted_token == stored_token:
            sub_email = request.form.get('femail')
            if sub_email:
                SubManager(email=sub_email)

    return redirect(url_for('index'))
