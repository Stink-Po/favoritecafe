#!/bin/python
from app import create_app


app = create_app()

with app.app_context():
    from app.methods.user_manager import UserManager
    from app.my_db_models.user_model import User
    from app.extentions import db
    user_mng = UserManager()
    all_users = db.session.query(User).all()
    for u in range(len(all_users) - 258):
        id = all_users[u].id
        user_mng.create_api_key(user_id=id)
    
    
    