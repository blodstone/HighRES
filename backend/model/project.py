import enum
from datetime import datetime

from backend.model import db, ma


class ProjectType(enum.Enum):
    ANNOTATION = 'Annotation'
    EVALUATION = 'Evaluation'


class BaseProject(object):
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(25), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime, nullable=True)

    is_active = db.Column(db.Boolean, nullable=False, default=True)


class EvaluationProject(BaseProject, db.Model):
    __tablename__ = 'evaluation_project'

    summ_group_id = db.Column(db.INTEGER, db.ForeignKey('summary_group.id'), nullable=False)
    highlight = db.Column(db.Boolean, default=True)
    # proj_statuses = db.relationship('ProjectStatus', backref='project', lazy=True)


class FluencyResult(db.Model):
    __tablename__ = 'fluency_result'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    finished_at = db.Column(db.DateTime, default=datetime.utcnow)
    opened_at = db.Column(db.DateTime, default=datetime.utcnow)
    validity = db.Column(db.Boolean, nullable=True, default=False)
    status_id = db.Column(db.INTEGER, db.ForeignKey('project_status.id'), nullable=False)
    mturk_code = db.Column(db.String(255), nullable=True)


class FluencyResultSchema(ma.ModelSchema):
    class Meta:
        model = FluencyResult
