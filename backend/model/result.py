from datetime import datetime
from backend.model import db, ma


class FluencyResult(db.Model):
    __tablename__ = 'fluency_result'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    fluency = db.Column(db.REAL, nullable=False, default=50.0)
    clarity = db.Column(db.REAL, nullable=False, default=50.0)
    proj_status_id = db.Column(db.INTEGER, db.ForeignKey('project_status.id'), nullable=False)
    summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=False)


class FluencyResultSchema(ma.ModelSchema):
    class Meta:
        model = FluencyResult
