from flask import render_template
from flask import g
from ..auth import login_required
from .base import admin
from . import gejala
from . import penyakit
from . import rule
from . import user

from app.model.Penyakit import Penyakit
from app.model.Gejala import Gejala
from app.model.MedicRecord import MedicRecord
from app.model import dbsession_required

@admin.route('/')
@login_required
@dbsession_required
def home():
    db_session = g.get('dbsession')
    data_rm = db_session.query(MedicRecord).all()
    data_penyakit = db_session.query(Penyakit).all()
    data_gejala = db_session.query(Gejala).all()
    count_penyakit = { p.nama: 0 for p in data_penyakit }
    count_gejala = { ge.id: 0 for ge in data_gejala }
    for rm in data_rm:
        pid = rm.meta['penyakit_id']
        print('pid=', pid)
        print(data_rm)
        penyakit = next((x for x in data_penyakit if x.id == pid), None)
        count_penyakit[penyakit.nama] += 1

        for ge in rm.list_gejala:
            count_gejala[ge.gejala.id] += 1

    penyakit_labels = list(count_penyakit.keys())
    penyakit_labels = sorted(penyakit_labels)
    penyakit_counts = [ count_penyakit[k] for k in penyakit_labels ]

    gejala_labels = list(count_gejala.keys())
    gejala_labels = sorted(gejala_labels)
    gejala_counts = [ count_gejala[k] for k in gejala_labels ]

    # Convert to json
    return render_template('index2.html',
                           penyakit_counts=penyakit_counts,
                           penyakit_labels=penyakit_labels,
                           gejala_labels=gejala_labels,
                           gejala_counts=gejala_counts)
