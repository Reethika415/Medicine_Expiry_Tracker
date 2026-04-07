from flask import Blueprint, render_template, request, redirect, url_for, session
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
