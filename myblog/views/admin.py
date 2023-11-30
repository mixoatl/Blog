from flask import Blueprint, flash, redirect, render_template, url_for
from myblog.models import user
from .auth import auth


admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@admin.route('/generate_report')
def generate_report():
    # Lógica para generar el informe
    total_users = user.User.query.count()
    flash(f'Reporte generado. Total de usuarios: {total_users}', 'success')
    return redirect(url_for('admin.admin_dashboard'))
