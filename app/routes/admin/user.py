from .base import admin

import datetime
import json
from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import Response

from app.model.User import User
from app.model.Rule import Rule
from app.model.Penyakit import Penyakit
from app.model.MedicRecord import MedicRecord
from app.model.GejalaMedicRecord import GejalaMedicRecord
from app.model import dbsession_required
from app.computation.vucr import vucr

PREFIX = '/users'

@admin.route(f"{PREFIX}")
@dbsession_required
def list_user():
    dbsession = g.get('dbsession')
    data = dbsession.query(User).filter(User.role != 'admin').all()
    return render_template('user/list.html', data=data)

@admin.route(f"{PREFIX}/create", methods=['GET', 'POST'])
@dbsession_required
def create_user():
    if request.method == 'GET':
        return render_template('user/create.html')

    nama = request.form['nama']
    user = User(nama=nama, role='user', username=nama)
    dbsession = g.get('dbsession')
    dbsession.add(user)
    dbsession.commit()
    return redirect(url_for('admin.list_user'))

@admin.route(f"{PREFIX}/detail/<id>", methods=['GET', 'POST'])
@dbsession_required
def detail_user(id):
    dbsession = g.get('dbsession')
    user = dbsession.query(User).filter(User.id == id).first()
    records = user.records
    list_penyakit = dbsession.query(Penyakit).all()
    record_penyakit_list = []
    for record in records:
        penyakit_id = record.meta['penyakit_id']
        for penyakit in list_penyakit:
            if penyakit.id == penyakit_id:
                record_penyakit_list.append(penyakit)

    # records_dict = []
    # for record in records:
    #     list_gejala = record.list_gejala
    #     list_gejala_dict = [ gejala.as_dict() for gejala in list_gejala ]
    #     record_dict = record.as_dict()
    #     records_dict.append(
    #         {
    #             **record_dict,
    #             'list_gejala': list_gejala_dict
    #         }
    #     )
    # data = {
    #     'user': user.as_dict(),
    #     'records': record_dict
    # }
    return render_template('user/detail.html', data=user, records=records, record_penyakit_list=record_penyakit_list)

@admin.route(f"{PREFIX}/diagnosa/<id>", methods=['GET', 'POST'])
@dbsession_required
def diagnosa_user(id):
    if request.method == 'GET':
        return render_template('user/diagnosa.html', user_id=id)

    content = request.json

    dbsession = g.get('dbsession')
    rules = dbsession.query(Rule).all()
    print('content=', content)
    gejala_list = content['gejala']
    list_gejala_id = [ gejala['id'] for gejala in gejala_list ]

    result = vucr(rules, list_gejala_id)

    medic_record_gejala = [
        GejalaMedicRecord(
            gejala_id=_gejala_id
        )
        for _gejala_id in list_gejala_id
    ]

    # Create medic record
    medic_record = MedicRecord(
        waktu=datetime.datetime.now(),
        meta=result,
        user_id=id,
        list_gejala=medic_record_gejala
    )

    dbsession.add(medic_record)
    dbsession.commit()

    response = Response(
        response='ok',
        status=200
    )
    return response