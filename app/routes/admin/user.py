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
    data = dbsession.query(User)\
        .filter(User.role != 'admin')\
        .join(MedicRecord, isouter=True)\
        .all()
    print(data)
    return render_template('user/list.html', data=data)

@admin.route(f"{PREFIX}/create", methods=['GET', 'POST'])
@dbsession_required
def create_user():
    if request.method == 'GET':
        return render_template('user/create.html')

    nama = request.form['nama']
    alamat = request.form['alamat']
    jk = request.form['jk'] == 'laki_laki'
    umur = int(request.form['umur'])
    user = User(nama=nama, role='user', username=nama, alamat=alamat, jk=jk, umur=umur)
    dbsession = g.get('dbsession')
    dbsession.add(user)
    dbsession.commit()
    return redirect(url_for('admin.list_user'))

@admin.route(f"{PREFIX}/update/<id>", methods=['GET', 'POST'])
@dbsession_required
def update_user(id):
    dbsession = g.get('dbsession')
    user = dbsession.query(User).filter(User.id == id).first()

    if request.method == 'GET':
        return render_template('user/update.html', data=user)

    nama = request.form['nama']
    alamat = request.form['alamat']
    jk = request.form['jk'] == 'laki_laki'
    umur = int(request.form['umur'])
    user.nama = nama
    user.alamat = alamat
    user.jk = jk
    user.umur = umur
    dbsession.add(user)
    dbsession.commit()
    return redirect(url_for('admin.detail_user', id=id))

@admin.route(f"{PREFIX}/detail/<id>", methods=['GET', 'POST'])
@dbsession_required
def detail_user(id):
    dbsession = g.get('dbsession')
    user = dbsession.query(User).filter(User.id == id).first()
    records = user.records
    list_penyakit = dbsession.query(Penyakit).all()
    record_penyakit_list = []
    for record in records:
        print('record_meta', record.meta)
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

    dbsession = g.get('dbsession')
    rules = dbsession.query(Rule).all()
    content = request.json

    print('content=', content)
    gejala_list = content['gejala']
    list_gejala_id = [ gejala['id'] for gejala in gejala_list ]

    result = vucr(rules, list_gejala_id)
    result_str = json.dumps(result)

    medic_record_gejala = [
        GejalaMedicRecord(
            gejala_id=_gejala_id
        )
        for _gejala_id in list_gejala_id
    ]

    # Create medic record
    medic_record = MedicRecord(
        waktu=datetime.datetime.now(),
        meta=result_str,
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


@admin.route(f"{PREFIX}/<id_user>/record/detail/<id_record>", methods=['GET', 'POST'])
@dbsession_required
def user_record_detail(id_user, id_record):
    dbsession = g.get('dbsession')

    pasien = dbsession.query(User).filter(User.id == id_user).first()
    if not pasien: raise Exception(f"Can't find pasien with id({id_user})")

    record = dbsession.query(MedicRecord).filter(MedicRecord.id == id_record).first()
    if not record: raise Exception(f"Can't find record with id({id_record})")

    list_gejala = [ _record_gejala.gejala for _record_gejala in record.list_gejala ]

    penyakit_id = record.meta['penyakit_id']
    penyakit = dbsession.query(Penyakit).filter(Penyakit.id == penyakit_id).first()
    if not penyakit: raise Exception(f"Can't find penyakit with id({penyakit_id})")

    return render_template('user/record-detail.html',
                            pasien=pasien,
                            list_gejala=list_gejala,
                            penyakit=penyakit,
                            record=record
                           )

@admin.route(f"{PREFIX}/<id_user>/record/delete/<id_record>")
@dbsession_required
def user_record_delete(id_user, id_record):
    dbsession = g.get('dbsession')
    dbsession.query(MedicRecord).filter_by(id=id_record).delete()
    dbsession.commit()
    return redirect(f"/admin/users/detail/{id_user}")

@admin.route(f"{PREFIX}/delete/<id_user>", methods=['GET', 'POST'])
@dbsession_required
def user_delete (id_user):
    dbsession = g.get('dbsession')
    dbsession.query(User).filter_by(id=id_user).delete()
    dbsession.commit()
    return redirect(url_for("admin.list_user"))
