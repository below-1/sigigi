# Import what we need
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template,
    request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from ..model import Gejala, Penyakit, User, MedicRecord, dbsession_required

bp = Blueprint('auth', __name__, url_prefix='/auth')


# Decorator to check if user is logged in.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function

def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        fallback = render_template('user/login.html')
        if 'user_id' not in session:
            return fallback
        if 'user_role' not in session:
            return fallback
        if session['user_role'] != 'user':
            return fallback
        return f(*args, **kwargs)

    return decorated_function

@bp.route('/signup/user', methods=["POST", "GET"])
@dbsession_required
def signup_user():
    if request.method == 'GET':
        return render_template('user/signup.html')

    dbsession = g.get('dbsession')
    username = request.form['username']
    nama_lengkap = request.form['nama_lengkap']
    password = request.form['password']
    password = generate_password_hash(password)

    user = User(
        username=username,
        nama_lengkap=nama_lengkap,
        password=password
    )

    dbsession.add(user)
    dbsession.commit()
    return redirect(url_for('user.home'))

@bp.route('/login', methods=['POST', 'GET'])
@dbsession_required
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        dbsession = g.get('dbsession')
        user = dbsession.query(User) \
            .filter(User.username == username) \
            .first()

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            session['user_role'] = user.role
            target = 'user.home'
            if user.role == 'admin':
                target = 'admin.home'
            return redirect(url_for(target))

        flash(error)
        return redirect(url_for('auth.login'))

    else:
        if session.get('user_id', None) is not None:
            target = 'user.home'
            if session.get('user_role') == 'admin':
                target = session.role
            return redirect(url_for(target))
        else:
            print('HERE')
            return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))