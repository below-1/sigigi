from .base import admin

import json
from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import Response

from ...model import Rule, Penyakit, Gejala, GejalaSlot
from ...model import dbsession_required

PREFIX = '/rules'

@admin.route(f"{PREFIX}")
@dbsession_required
def list_rules():
    dbsession = g.get('dbsession')
    data = dbsession.query(Rule).all()
    print('data=', data)
    return render_template('rules/list.html', data=data)

@admin.route(f"{PREFIX}/create", methods=['GET', 'POST'])
@dbsession_required
def create_rule():
    dbsession = g.get('dbsession')
    if request.method == 'GET':
        list_penyakit = dbsession.query(Penyakit).filter(Penyakit.deleted == False).all()
        list_gejala = dbsession.query(Gejala).filter(Gejala.deleted == False).all()

        _VUE_list_gejala = [ gej.as_dict() for gej in list_gejala ]
        for gej in _VUE_list_gejala:
            gej['weight'] = 0
            gej['selected'] = False

        VUE_list_penyakit = ','.join([ json.dumps(p.as_dict()) for p in list_penyakit ])
        VUE_list_gejala = ','.join([ json.dumps(gej) for gej in _VUE_list_gejala ])

        return render_template(
            'rules/create.html',
            list_gejala=list_gejala,
            list_penyakit=list_penyakit,
            vue={
                'list_penyakit': VUE_list_penyakit,
                'list_gejala': VUE_list_gejala
            }
        )

    content = request.json
    print('content=', content)
    penyakit_id = content['penyakit_id']
    gejala_payload = content['gejala']

    rule = Rule(
        penyakit_id=int(penyakit_id)
    )
    dbsession.add(rule)
    dbsession.commit()
    rule_id = rule.id

    for slot_input in gejala_payload:
        weight = float( slot_input['weight'] )
        gid = int(slot_input['id'])
        _slot = GejalaSlot(rule_id=rule_id, gejala_id=gid,weight=weight)
        dbsession.add(_slot)
    dbsession.commit()
    return redirect(url_for('admin.list_rules'))

@admin.route(f"{PREFIX}/delete/<id>")
@dbsession_required
def delete_rule(id):
    dbsession = g.get('dbsession')
    dbsession.query(Rule).filter(Rule.id == id).delete()
    dbsession.commit()
    return redirect(url_for('admin.list_rules'))


@admin.route(f"{PREFIX}/update/<id>", methods=['GET', 'POST'])
@dbsession_required
def update_rule(id):
    if request.method == 'GET':
        return render_template('rules/update.html', id=id)

    dbsession = g.get('dbsession')
    content = request.json
    penyakit_id = content['penyakit_id']
    list_gejala_dict = content['gejala']

    # Response result
    result = 'Error'
    status = 500

    try:
        dbsession.query(Rule).filter(Rule.id == id).delete()

        slot_list = []
        for _dict in list_gejala_dict:
            if not _dict['selected']: continue
            new_slot = GejalaSlot(
                gejala_id=int(_dict['id']),
                weight=float(_dict['weight'])
            )
            slot_list.append(new_slot)

        new_rule = Rule(
            penyakit_id=penyakit_id,
            slots=slot_list
        )
        dbsession.add(new_rule)
        dbsession.commit()

        status = 200
        result = 'OK'

    except Exception as ex:
        print(f"exception happens: {ex}")
        dbsession.rollback()
        # reraise exception
        raise Exception("Stop here")

    response = Response(
        response=result,
        status=status,
        mimetype='application/json'
    )

    return response