from backend.model import db, ma
from backend.model.summary import SummaryGroupSchema


class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    summ_groups = db.relationship('SummaryGroup', backref='dataset', lazy=True)


class DatasetSchema(ma.ModelSchema):
    class Meta:
        model = Dataset
    summ_groups = ma.Nested(SummaryGroupSchema, many=True)
