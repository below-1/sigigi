from .base import admin

import json
from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from app.model.User import User
from app.model import dbsession_required

PREFIX = '/users'

@admin.route(f"{PREFIX}")
@dbsession_required
def list_user():
    dbsession = g.get('dbsession')
    data = dbsession.query(User).filter(User.role != 'admin').all()
    return render_template('user/list.html', data=data)