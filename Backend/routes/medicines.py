from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Medicine, FamilyMember, Category
from datetime import date, timedelta

medicines = Blueprint('medicines', __name__)

@medicines.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    uid = session['user_id']from flask import (Blueprint, render_template,
    request, redirect, url_for, session)
from models import db, Medicine, FamilyMember, Category
from datetime import date, timedelta

medicines = Blueprint('medicines', __name__)

@medicines.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    uid = session['user_id']
    today = date.today()
    soon = today + timedelta(days=30)
    
    from sqlalchemy import text
    
    all_meds = db.session.execute(text("""
        SELECT m.medicine_id, m.name,
               f.name as member_name,
               c.name as category_name,
               m.expiry_date, m.status,
               m.quantity
        FROM medicines m
        JOIN familymembers f 
             ON m.member_id = f.member_id
        JOIN categories c 
             ON m.category_id = c.category_id
        WHERE m.user_id = :uid
    """), {'uid': uid}).fetchall()
    
    expiring_count = db.session.execute(text("""
        SELECT COUNT(*) FROM medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date BETWEEN :today 
        AND :soon
    """), {'uid': uid,
           'today': today,
           'soon': soon}).scalar()
    
    expired_count = db.session.execute(text("""
        SELECT COUNT(*) FROM medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date < :today
    """), {'uid': uid,
           'today': today}).scalar()
    
    safe_count = db.session.execute(text("""
        SELECT COUNT(*) FROM medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date > :soon
    """), {'uid': uid,
           'soon': soon}).scalar()
    
    return render_template('dashboard.html',
        medicines=all_meds,
        expiring=expiring_count,
        expired=expired_count,
        safe=safe_count,
        today=today,
        timedelta=timedelta)


@medicines.route('/add', methods=['GET', 'POST'])
def add_medicine():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        new_med = Medicine(
            user_id=session['user_id'],
            member_id=request.form['member_id'],
            category_id=request.form['category_id'],
            name=request.form['name'],
            quantity=request.form['quantity'],
            purchase_date=request.form['purchase_date'],
            expiry_date=request.form['expiry_date']
        )
        db.session.add(new_med)
        db.session.commit()
        return redirect(url_for('medicines.dashboard'))
    
    members = FamilyMember.query.filter_by(
        user_id=session['user_id']).all()
    categories = Category.query.all()
    
    return render_template(
        'add_medicine.html',
        members=members,
        categories=categories
    )
    today = date.today()
    soon = today + timedelta(days=30)

    all_meds = Medicine.query.filter_by(user_id=uid).all()

    expiring = Medicine.query.filter(
        Medicine.user_id == uid,
        Medicine.expiry_date <= soon,
        Medicine.expiry_date >= today
    ).all()

    expired = Medicine.query.filter(
        Medicine.user_id == uid,
        Medicine.expiry_date < today
    ).all()

    return render_template(
        'dashboard.html',
        medicines=all_meds,
        expiring=expiring,
        expired=expired,
        today=today,
        timedelta=timedelta
    )


@medicines.route('/add', methods=['GET', 'POST'])
def add_medicine():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        new_med = Medicine(
            user_id=session['user_id'],
            member_id=request.form['member_id'],
            category_id=request.form['category_id'],
            name=request.form['name'],
            quantity=request.form['quantity'],
            purchase_date=request.form['purchase_date'],
            expiry_date=request.form['expiry_date']
        )

        db.session.add(new_med)
        db.session.commit()

        return redirect(url_for('medicines.dashboard'))

    members = FamilyMember.query.filter_by(user_id=session['user_id']).all()
    categories = Category.query.all()

    return render_template(
        'add_medicine.html',
        members=members,
        categories=categories
    )
