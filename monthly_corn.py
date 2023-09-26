#!/bin/python
from app import create_app


app = create_app()

with app.app_context():
  
    from app.methods.user_manager import UserManager
    from app.methods.send_mail import SendEmailtononActiveMembers

    user_mng = UserManager()
    email_list = user_mng.find_non_active_users()
    for user_info in email_list:
        email_sender = SendEmailtononActiveMembers(username=user_info[0], email=user_info[1])
        email_sender.send_email()
