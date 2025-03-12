from database import get_db
from database.models import *
def add_user_db(username, phone_number, email, password, city=None, birthday=None):
    with next(get_db()) as db:
        check = db.query(User).filter_by(phone_number=phone_number).all()
        if check:
            return {'status': 0, 'message': 'This phone number is already used'}
        check = db.query(User).filter_by(email=email).all()
        if check:
            return {'status': 0, 'message': 'This email is already used'}
        check = db.query(User).filter_by(username=username).all()
        if check:
            return {'status': 0, 'message': 'This username is already used'}
        new_user = User(username=username, phone_number=phone_number, email=email, password=password, city=city,
                        birthday=birthday)
        db.add(new_user)
        db.commit()
        return new_user.id
def add_user_db2(username, phone_number, email, password, city=None, birthday=None):
    with next(get_db()) as db:
        phone = db.query(User).filter_by(phone_number=phone_number).all()
        email = db.query(User).filter_by(email=email).all()
        name = db.query(User).filter_by(username=username).all()
        text = ""
        if name:
            text += "\n-username"
        if phone:
            text += "\n-phone number"
        if email:
            text += "\n-email"
        text += "\nis/are already used"
        if phone or email or name:
            return {'status': 0, 'message': text}
        new_user = User(username=username, phone_number=phone_number, email=email, password=password, city=city,
                        birthday=birthday)
        db.add(new_user)
        db.commit()
        return new_user.id


def login_db(name, ph_number, password, email):
    db = next(get_db())
    check = db.query(User).filter_by(username=name).first()
    if not check:
        check = db.query(User).filter_by(phone_number=ph_number).first()
        if not check:
            check = db.query(User).filter_by(email=email).first()
            if not check:
                return {'status':0, 'message': 'failed'}
    if check.password == password:
        return {'status':1, 'message': check.id}