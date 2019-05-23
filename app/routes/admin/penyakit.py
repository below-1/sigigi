from .base import admin

import json
from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from ...model import Penyakit
from ...model import dbsession_required

PREFIX = '/diseases'

@admin.route(f"{PREFIX}")
@dbsession_required
def list_penyakit():
    dbsession = g.get('dbsession')
    data = dbsession.query(Penyakit).order_by(Penyakit.nama).all()
    return render_template('penyakit/list.html', data=data)
    pass

@admin.route(f"{PREFIX}/create", methods=['GET', 'POST'])
@dbsession_required
def add_penyakit():
    if request.method == 'GET':
        return render_template('penyakit/create.html')
    elif request.method == 'POST':
        dbsession = g.get('dbsession')
        nama = request.form['nama']
        keterangan = request.form['keterangan']
        penyakit = Penyakit(
            nama=nama,
            keterangan=keterangan
        )
        dbsession.add(penyakit)
        dbsession.commit()
        return redirect(url_for('admin.list_penyakit'))

@admin.route(f"{PREFIX}/delete/<id>")
@dbsession_required
def delete_penyakit(id):
    dbsession = g.get('dbsession')
    dbsession.query(Penyakit).filter(Penyakit.id == id).delete()
    dbsession.commit()
    return redirect(url_for('admin.list_penyakit'))

@admin.route(f"{PREFIX}/update/<id>", methods=['GET', 'POST'])
@dbsession_required
def update_penyakit(id):
    dbsession = g.get('dbsession')
    if request.method == 'GET':
        penyakit = dbsession.query(Penyakit).filter(Penyakit.id == id).first()
        return render_template('penyakit/edit.html', data=penyakit)
    elif request.method == 'POST':
        penyakit = dbsession.query(Penyakit).filter(Penyakit.id == id).first()
        penyakit.nama = request.form['nama']
        penyakit.keterangan = request.form['keterangan']
        dbsession.commit()
        return redirect(url_for('admin.list_penyakit'))

@admin.route(f"{PREFIX}/<id>")
@dbsession_required
def get_penyakit(id):
    dbsession = g.get('dbsession')
    pass