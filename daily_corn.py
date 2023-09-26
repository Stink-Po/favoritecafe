#!/bin/python
from app import create_app
from app.my_db_models import User

app = create_app()

with app.app_context():
    # Your code that requires access to db.session or other Flask components
    from app.extentions import db
    from app.my_db_models import User

    all_users = db.session.query(User).all()

    for user in all_users:
        user.daily_api_call = 0
        try:
            db.session.commit()
    
        except Exception as e:
            db.session.rollback()
            print(e.args)
