import datetime
from backend.model import db, ma


class FluencyResultList(db.Model):
    __tablename__ = 'fluency_result_list'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    finished_at = db.Column(db.DateTime, default=datetime.utcnow)
    opened_at = db.Column(db.DateTime, default=datetime.utcnow)
    mturk_code = db.Column(db.String(255), nullable=True)


class FluencyResult(db.Model):
    __tablename__ = 'fluency_result'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    proj_status_id = db.Column(db.INTEGER, db.ForeignKey('project_status.id'), nullable=False)
    fluency_result_list_id = db.Column(db.INTEGER, db.ForeignKey('fluency_result_list.id'), nullable=False)


class FluencyResultListSchema(ma.ModelSchema):
    class Meta:
        model = FluencyResultList


class FluencyResultSchema(ma.ModelSchema):
    class Meta:
        model = FluencyResult
