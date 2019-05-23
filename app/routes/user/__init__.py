from .base import user_bp
from flask import g
from flask import render_template
from flask import request
from app.model.Rule import Rule
from app.routes.auth import user_required
from app.computation.vucr import vucr

@user_bp.route('/')
@user_required
def home():
    return render_template("home/index.html")


@user_bp.route('/diagnosa', methods=['GET', 'POST'])
@user_required
def diagnosa():
    # Load all rules
    dbsession = g.get('dbsession')

    if request.method == 'GET':
        return render_template('user/diagnosa.html')

    rules = dbsession.query(Rule).all()
    result = vucr(rules)
    return 'Ok'
