from flask import Blueprint, render_template, flash, redirect, url_for, session
import os

home_bp = Blueprint('home',__name__, template_folder='templates')

@home_bp.route('/')
def home_page():
    cwd = os.getcwd()
    return render_template('home.html',cwd=cwd)

@home_bp.route('/clear_session')
def clear_session():
    session.clear()
    flash('All Clear!',category='success')
    return redirect(url_for('home.home'))
