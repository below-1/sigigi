from .base import admin

import json
from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from ...model import Gejala
from ...model import dbsession_required

PREFIX = '/symptoms'

@admin.route(PREFIX, methods=['GET'])
@dbsession_required
def list_gejala():
    dbsession = g.get('dbsession')
    data = dbsession.query(Gejala).filter(Gejala.deleted == False).order_by(Gejala.nama).all()
    return render_template('gejala/list.html', data=data)

@admin.route(f"{PREFIX}/create", methods=['GET', 'POST'])
@dbsession_required
def create_gejala():
    if request.method == 'GET':
        return render_template('gejala/create.html')
    elif request.method  == 'POST':
        dbsession = g.get('dbsession')
        nama = request.form['nama']
        keterangan = request.form['keterangan']

        gejala = Gejala(
            nama=nama,
            keterangan=keterangan
        )

        dbsession.add(gejala)
        dbsession.commit()
        return redirect(url_for('admin.list_gejala'))

@admin.route(f"{PREFIX}/delete/<id>", methods=['GET'])
@dbsession_required
def delete_gejala(id):
    dbsession = g.get('dbsession')
    gejala = dbsession.query(Gejala).filter(Gejala.id == id).first()
    gejala.deleted = True
    dbsession.commit()
    return redirect(url_for('admin.list_gejala'))

@admin.route(f"{PREFIX}/update/<id>", methods=['GET', 'POST'])
@dbsession_required
def update_gejala(id):
    dbsession = g.get('dbsession')
    if request.method == 'GET':
        data = dbsession.query(Gejala).filter(Gejala.id == id).first()
        return render_template('gejala/edit.html', data=data)
    elif request.method == 'POST':
        data = dbsession.query(Gejala).filter(Gejala.id == id).first()
        data.nama = request.form['nama']
        data.keterangan = request.form['keterangan']
        dbsession.commit()
        return redirect(url_for('admin.list_gejala'))