from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, User,FamilyMember

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

        if user and  user.password==password:
            session['user_id'] = user.user_id
            session['user_name'] = user.name
            return redirect(url_for('medicines.dashboard'))

        return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            new_user = User(
                name=request.form['name'],
                email=request.form['email'],
                password=request.form['password'],
                phone=request.form['phone']
            )
            db.session.add(new_user)
            db.session.flush()  # Gets new_user.user_id WITHOUT full commit

            default_members = [
                FamilyMember(user_id=new_user.user_id, name='Self', age=25, relation='Self'),
                FamilyMember(user_id=new_user.user_id, name='Mom', age=50, relation='Mother'),
                FamilyMember(user_id=new_user.user_id, name='Dad', age=55, relation='Father'),
                FamilyMember(user_id=new_user.user_id, name='Sister', age=20, relation='Sister'),
                FamilyMember(user_id=new_user.user_id, name='Brother', age=22, relation='Brother'),
                FamilyMember(user_id=new_user.user_id, name='Grandmother', age=70, relation='Grandmother'),
                FamilyMember(user_id=new_user.user_id, name='Grandfather', age=72, relation='Grandfather'),
            ]
            for member in default_members:
                db.session.add(member)

            db.session.commit()  # Single commit for everything
            print(f"✅ Registered {new_user.name} with 7 family members")

        except Exception as e:
            db.session.rollback()
            print(f"❌ Registration error: {e}")

        return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
