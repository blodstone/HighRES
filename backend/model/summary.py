from backend.model import db, ma


class Summary(db.Model):
    __tablename__ = 'summary'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    text = db.Column(db.Text, nullable=False)

    summary_group_id = db.Column(db.INTEGER, db.ForeignKey('summary_group.id'), nullable=False)
    doc_id = db.Column(db.INTEGER, db.ForeignKey('document.id'), nullable=False)

    # summary_statuses = db.relationship('SummaryStatus', backref='summary', lazy=True)


class SummarySchema(ma.ModelSchema):
    class Meta:
        model = Summary


class SummaryGroup(db.Model):
    """
    For different model or reference group
    """
    __tablename__ = 'summary_group'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    is_ref = db.Column(db.Boolean, nullable=False, default=False)

    dataset_id = db.Column(db.INTEGER, db.ForeignKey('dataset.id'), nullable=False)
    summaries = db.relationship('Summary', backref='summary_group')


class SummaryGroupSchema(ma.ModelSchema):
    class Meta:
        model = SummaryGroup
        include_fk = True


class SanitySummary(db.Model):
    """
    For sanity checking where user's submission is deemed valid
    if the best_summary >= avg_summary > worst_summary
    """
    __tablename__ = 'sanity_summary'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    best_summary = db.Column(db.Text, nullable=False)
    avg_summary = db.Column(db.Text, nullable=False)
    worst_summary = db.Column(db.Text, nullable=False)

    dataset_id = db.Column(db.INTEGER, db.ForeignKey('dataset.id'), nullable=False)


class SanitySummarySchema(ma.ModelSchema):
    class Meta:
        model = SanitySummary
