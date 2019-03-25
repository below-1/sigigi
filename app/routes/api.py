# Import what we need
import json
from flask import (
    Blueprint, flash, g, redirect, render_template,
    request, session, url_for, jsonify, current_app,
    Response
)
from ..model import Gejala, Penyakit, User, MedicRecord, dbsession_required, Rule

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/gejala', methods=['POST'])
@dbsession_required
def gejala_create():
    content = request.json
    nama = content['nama']
    keterangan = content['keterangan']
    gejala = Gejala(
        nama=nama,
        keterangan=keterangan
    )

    dbsession = g.get('dbsession')
    dbsession.add(gejala)
    dbsession.commit()

    response = Response(
        response=json.dumps(gejala.as_dict()),
        status=200,
        mimetype='application/json'
    )

    return response


@api.route('/gejala', methods=['GET'])
@dbsession_required
def gejala_get_all():
    dbsession = g.get('dbsession')
    list_gejala = dbsession.query(Gejala).all()
    json_gejala = list(map(lambda gejala: gejala.as_dict(), list_gejala))
    return Response(
        response=json.dumps(json_gejala),
        status=201,
        mimetype='application/json'
    )

@api.route('/gejala/<id>', methods=['GET'])
@dbsession_required
def gejala_get_one(id):
    dbsession = g.get('dbsession')
    gejala = dbsession.query(Gejala).filter(Gejala.id == id).first()
    response = Response(
        response=json.dumps(gejala.as_dict()),
        status=200,
        mimetype='application/json'
    )
    return response

@api.route('/gejala/<id>', methods=['PUT'])
@dbsession_required
def gejala_update(id):
    dbsession = g.get('dbsession')
    gejala = dbsession.query(Gejala).filter(Gejala.id == id).first()
    content = request.json
    gejala.nama = content['nama']
    gejala.keterangan = content['keterangan']
    dbsession.save(gejala)
    dbsession.commit()

    response = Response(
        response=json.dumps(gejala.as_dict()),
        status=200,
        mimetype='application/json'
    )
    return response

@api.route('/gejala/<id>', methods=['DELETE'])
@dbsession_required
def gejala_delete(id):
    dbsession = g.get('dbsession')
    dbsession.query(Gejala).filter(Gejala.id == id).delete()
    dbsession.commit()
    return 'ok'

@api.route('/penyakit', methods=['POST'])
@dbsession_required
def penyakit_create():
    content = request.json
    penyakit = Penyakit(
        nama=content['nama'],
        keterangan=content['keterangan']
    )

    dbsession = g.get('dbsession')
    dbsession.add(penyakit)
    dbsession.commit()

    response = Response(
        response=json.dumps(penyakit.as_dict()),
        status=201,
        mimetype='application/json'
    )

    return response

@api.route('/rules/<id>')
@dbsession_required
def get_Rule_Data(id: int):
    dbsession = g.get('dbsession')
    rule = dbsession.query(Rule).filter(Rule.id == id).first()
    rule_slots = rule.slots

    all_gejala = dbsession.query(Gejala).filter(Gejala.deleted == False).all()
    all_penyakit = dbsession.query(Penyakit).filter(Penyakit.deleted == False).all()

    list_penyakit = []
    for penyakit in all_penyakit:
        penyakit_dict = penyakit.as_dict()
        if penyakit.id == rule.penyakit_id:
            penyakit_dict['selected'] = True
        else:
            penyakit_dict['selected'] = False
        list_penyakit.append(penyakit_dict)

    list_gejala = []
    for gejala in all_gejala:
        gej_dict = gejala.as_dict()
        gej_dict['weight'] = 0
        gej_dict['selected'] = False
        for slot in rule_slots:
            if slot.gejala_id == gejala.id:
                gej_dict['weight'] = slot.weight
                gej_dict['selected'] = True
                break
        list_gejala.append(gej_dict)

    json_rule = rule.as_dict()
    result = { **json_rule, 'list_gejala': list_gejala, 'list_penyakit': list_penyakit }

    response = Response(
        response=json.dumps(result),
        mimetype='application/json',
        status=200
    )

    return response


def update_Rule_Data(id):
    dbsession = g.get('dbsession')

    pass
# @api.route('/penyakit', methods=['GET'])
# @dbsession_required
# def penyakit_get_all():
#     pass
#
# @api.route('/penyakit/<id>', methods=['GET'])
# @dbsession_required
# def penyakit_get_all(id):
#     pass
#
# @api.route('/penyakit/<id>', methods=['PUT'])
# @dbsession_required
# def penyakit_get_all(id):
#     pass