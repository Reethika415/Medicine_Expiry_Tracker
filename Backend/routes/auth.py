from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.user_id
            session['user_name'] = user.name
            return redirect(url_for('medicines.dashboard'))

        return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password'],
            phone=request.form['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
