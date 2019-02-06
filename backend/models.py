"""
SQL Alchemy model
"""
import json
from enum import Enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()


class Dataset(db.Model):
    """
    A dataset
    """
    __tablename__ = 'dataset'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def get(self):
        return