from backend.model import db, ma


class FluencyResult(db.Model):
    __tablename__ = 'fluency_result'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    fluency = db.Column(db.REAL, nullable=False, default=50.0)
    is_invalid = db.Column(db.Boolean, default=False)
    proj_status_id = db.Column(db.INTEGER, db.ForeignKey('project_status.id'), nullable=False)
    summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=False)


class FluencyResultSchema(ma.ModelSchema):
    class Meta:
        model = FluencyResult
        include_fk = True


class ClarityResult(db.Model):
    __tablename__ = 'clarity_result'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    clarity = db.Column(db.REAL, nullable=False, default=50.0)
    is_invalid = db.Column(db.Boolean, default=False)
    proj_status_id = db.Column(db.INTEGER, db.ForeignKey('project_status.id'), nullable=False)
    summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=False)


class ClarityResultSchema(ma.ModelSchema):
    class Meta:
        model = ClarityResult
        include_fk = True
