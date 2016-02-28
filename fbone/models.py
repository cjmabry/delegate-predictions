# -*- coding: utf-8 -*-

from sqlalchemy import Column, types
from sqlalchemy.ext.mutable import Mutable
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from extensions import db
from utils import get_current_time, SEX_TYPE, STRING_LEN

class Poll(db.Model):
    __tablename__ = 'polls'

    id = Column(db.Integer, primary_key=True)

    state = Column(db.String(3), nullable=False, unique=False)
    clinton = Column(db.Float(), nullable=False)
    sanders = Column(db.Float(), nullable=False)
    undecided = Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime)

class State(db.Model):
    __tablename__ = 'states'

    id = Column(db.Integer, primary_key=True)

    state = Column(db.String(3), nullable=False, unique=False)
    pledged_available = Column(db.Integer())
    unpledged_available = Column(db.Integer())
    total_available = Column(db.Integer())
    clinton_percentage = Column(db.Float())
    sanders_percentage = Column(db.Float())
    clinton_delegates = Column(db.Float())
    sanders_delegates = Column(db.Float())
    clinton_percentage_results = Column(db.Float())
    sanders_percentage_results = Column(db.Float())
    clinton_delegates_results = Column(db.Float())
    sanders_delegates_results = Column(db.Float())
    url = Column(db.String(STRING_LEN))
    election_date = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)

class Daily(db.Model):
    __tablename__ = 'daily'

    id = Column(db.Integer, primary_key=True)

    state = Column(db.String(3), nullable=False)
    date = db.Column(db.DateTime)
    clinton_percentage = Column(db.Float())
    sanders_percentage = Column(db.Float())
