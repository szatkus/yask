import string
import random

from sqlalchemy import Column, String
from flask import request, render_template

from app import app
from database import Base, atomic
from mail import send_mail
from users import User

class RegistrationCode(Base):
    __tablename__ = 'registration_code'

    value = Column(String(length=32), nullable=False, primary_key=True)

def generate_password():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

@app.route('/register', methods=['GET'])
def register_view():
    print(render_template('register.html'))
    return render_template('register.html')

@app.route('/register', methods=['POST'])
@atomic
def register(session):
    code = session.query(RegistrationCode).filter_by(value=request.form['code']).scalar()
    if code is not None:
        email_address = request.form['email']
        user = User()
        user.username = request.form['username']
        password = generate_password()
        user.password = password
        user.email = email_address
        user.role = 'user'
        session.add(user)
        session.delete(code)
        send_mail('registration_email.html', 'Przenieś to potem gdzieś', email_address, password=password, username=user.username)
        result = 'ok'
    else:
        result = 'wrong_code'

    return render_template('register.html', result=result)
