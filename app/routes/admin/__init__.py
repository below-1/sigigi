from flask import render_template
from ..auth import login_required
from .base import admin
from . import gejala
from . import penyakit
from . import rule
from . import user

@admin.route('/')
@login_required
def home():
    return render_template('index2.html')
