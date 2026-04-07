from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from models import Medicine
from datetime import date, timedelta

alerts = Blueprint('alerts', __name__)

@alerts.route('/alerts')
def view_alerts():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    uid = session['user_id']
    today = date.today()
    soon = today + timedelta(days=30)

    expiring = Medicine.query.filter(
        Medicine.user_id == uid,
        Medicine.expiry_date <= soon
    ).all()

    return render_template('alerts.html', alerts=expiring, today=today)


@alerts.route('/analytics')
def analytics():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    return render_template('analytics.html')


@alerts.route('/api/check-expiry')
def check_expiry():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'})

    uid = session['user_id']
    today = date.today()
    soon = today + timedelta(days=30)

    expiring = Medicine.query.filter(
        Medicine.user_id == uid,
        Medicine.expiry_date <= soon,
        Medicine.expiry_date >= today
    ).count()

    expired = Medicine.query.filter(
        Medicine.user_id == uid,
        Medicine.expiry_date < today
    ).count()

    return jsonify({
        'expiring_soon': expiring,
        'expired': expired
    })
