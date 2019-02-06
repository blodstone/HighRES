from backend.model import db, ma


class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)


class DatasetSchema(ma.ModelSchema):
    class Meta:
        model = Dataset
