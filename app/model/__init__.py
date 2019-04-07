from functools import wraps

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash
import click

from app.config import DATABASE_URI
from app.model.base import Base
from app.model.Gejala import Gejala
from app.model.GejalaSlot import GejalaSlot
from app.model.GejalaMedicRecord import GejalaMedicRecord
from app.model.Penyakit import Penyakit
from app.model.User import User
from app.model.Rule import Rule
from app.model.MedicRecord import MedicRecord

_engine = create_engine(DATABASE_URI)
_DbSession = sessionmaker(autoflush=True)

def _create_session():
    db_session = _DbSession(bind=_engine)
    return db_session


@click.command('init-db')
@with_appcontext
def init_db():
    print(DATABASE_URI)
    print(Base.metadata.create_all(_engine))
    dbsession = _create_session()
    phash = generate_password_hash('admin')
    admin = User(
        username='admin',
        role='admin',
        password=phash
    )
    dbsession.add(admin)
    dbsession.commit()


def dbsession_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        dbsession = g.pop('dbsession', None)
        if dbsession is None:
            g.dbsession = _create_session()
        return f(*args, **kwargs)
    return wrap

# Remove the session from request context and close it.
# What the fuck is 'e'
def close_session(e=None):
    session = g.pop('dbsession', None)
    if session is not None:
        session.close()

# Register session lifecycle hook to instance.
# Using function since we use factory.
def init_app(app=None):
    if app is None: raise Exception('App is none!')
    app.teardown_appcontext(close_session)
    app.cli.add_command(init_db)