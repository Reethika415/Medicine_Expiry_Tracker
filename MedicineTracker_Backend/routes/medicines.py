from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models import db, Medicine, FamilyMember, Category, User
from datetime import date, timedelta
import pandas as pd

medicines = Blueprint('medicines', __name__)

# Load medicine names from CSV once at startup
try:
    med_df = pd.read_csv('A_Z_medicines_dataset_of_India.csv')
    VALID_MEDICINES = set(med_df['name'].str.lower().str.strip().tolist())
    print(f"✅ Loaded {len(VALID_MEDICINES)} medicine names")
except Exception as e:
    VALID_MEDICINES = set()
    print(f"❌ Could not load medicines CSV: {e}")

@medicines.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    uid = session['user_id']
    today = date.today()
    soon = today + timedelta(days=90)
    from sqlalchemy import text
    all_meds = db.session.execute(text("""
        SELECT m.medicine_id, m.name,
               f.name as member_name,
               c.name as category_name,
               m.expiry_date, m.status,
               m.quantity
        FROM Medicines m
        JOIN FamilyMembers f ON m.member_id = f.member_id
        JOIN Categories c ON m.category_id = c.category_id
        WHERE m.user_id = :uid
    """), {'uid': uid}).fetchall()
    expiring_count = db.session.execute(text("""
        SELECT COUNT(*) FROM Medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date BETWEEN :today AND :soon
    """), {'uid': uid, 'today': today, 'soon': soon}).scalar()
    expired_count = db.session.execute(text("""
        SELECT COUNT(*) FROM Medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date < :today
    """), {'uid': uid, 'today': today}).scalar()
    safe_count = db.session.execute(text("""
        SELECT COUNT(*) FROM Medicines m
        WHERE m.user_id = :uid
        AND m.expiry_date > :soon
    """), {'uid': uid, 'soon': soon}).scalar()
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
    members = FamilyMember.query.filter_by(user_id=session['user_id']).all()
    categories = Category.query.all()
    return render_template('add_medicine.html', members=members, categories=categories)

@medicines.route('/edit/<int:med_id>', methods=['GET', 'POST'])
def edit_medicine(med_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    medicine = Medicine.query.filter_by(medicine_id=med_id, user_id=session['user_id']).first_or_404()
    if request.method == 'POST':
        medicine.name = request.form['name']
        medicine.member_id = request.form['member_id']
        medicine.category_id = request.form['category_id']
        medicine.quantity = request.form['quantity']
        medicine.purchase_date = request.form['purchase_date']
        medicine.expiry_date = request.form['expiry_date']
        db.session.commit()
        return redirect(url_for('medicines.dashboard'))
    members = FamilyMember.query.filter_by(user_id=session['user_id']).all()
    categories = Category.query.all()
    return render_template('edit_medicine.html', medicine=medicine, members=members, categories=categories)

@medicines.route('/delete/<int:med_id>')
def delete_medicine(med_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    medicine = Medicine.query.filter_by(medicine_id=med_id, user_id=session['user_id']).first_or_404()
    db.session.delete(medicine)
    db.session.commit()
    return redirect(url_for('medicines.dashboard'))

@medicines.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.get(session['user_id'])
        if user.password != data['current_password']:
            return jsonify({'success': False, 'error': 'Current password is incorrect'})
        if data['new_password'] != data['confirm_password']:
            return jsonify({'success': False, 'error': 'New passwords do not match'})
        if len(data['new_password']) < 6:
            return jsonify({'success': False, 'error': 'Password must be at least 6 characters'})
        user.password = data['new_password']
        db.session.commit()
        return jsonify({'success': True})
    return render_template('change_password.html')

@medicines.route('/api/validate-medicine')
def validate_medicine():
    name = request.args.get('name', '').strip().lower()
    if not name or len(name) < 3:
        return jsonify({'valid': False, 'message': 'Please enter at least 3 characters'})
    
    # Exact match
    if name in VALID_MEDICINES:
        return jsonify({'valid': True, 'message': 'Valid medicine name ✅'})
    
    # Partial match — accept if typed name is found within any medicine name
    partial_matches = [m for m in VALID_MEDICINES if name in m]
    if partial_matches:
        return jsonify({'valid': True, 'message': f'Valid medicine name ✅'})
    
    # Suggestions for close matches
    suggestions = [m for m in VALID_MEDICINES if m.startswith(name[:4])][:3]
    if suggestions:
        return jsonify({'valid': False, 'message': f'Not found. Did you mean: {", ".join(suggestions)}?'})
    
    return jsonify({'valid': True, 'message': 'Medicine name accepted ✅'})
@medicines.route('/api/check-expiry')
def check_expiry():
    if 'user_id' not in session:
        return jsonify({})
    uid = session['user_id']
    today = date.today()
    soon = today + timedelta(days=90)
    from sqlalchemy import text
    expiring = db.session.execute(text("""
        SELECT COUNT(*) FROM Medicines WHERE user_id=:uid
        AND expiry_date BETWEEN :today AND :soon
    """), {'uid': uid, 'today': today, 'soon': soon}).scalar()
    expired = db.session.execute(text("""
        SELECT COUNT(*) FROM Medicines WHERE user_id=:uid
        AND expiry_date < :today
    """), {'uid': uid, 'today': today}).scalar()
    return jsonify({'expiring_soon': expiring, 'expired': expired})
