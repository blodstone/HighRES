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


class SummaryGroupList(db.Model):
    """
    N-to-N table linking project and summary group
    """
    __tablename__ = 'summary_group_list'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    fluency_proj_id = db.Column(db.INTEGER, db.ForeignKey('fluency_project.id'), nullable=True)
    clarity_proj_id = db.Column(db.INTEGER, db.ForeignKey('clarity_project.id'), nullable=True)
    summ_group_id = db.Column(db.INTEGER, db.ForeignKey('summary_group.id'), nullable=False)


class SanitySummary(db.Model):
    """
    For sanity checking where user's submission is deemed valid
    if the good_summary >= mediocre_summary > bad_summary
    """
    __tablename__ = 'sanity_summary'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    good_summary = db.Column(db.Text, nullable=False)
    mediocre_summary = db.Column(db.Text, nullable=False)
    bad_summary = db.Column(db.Text, nullable=False)

    dataset_id = db.Column(db.INTEGER, db.ForeignKey('dataset.id'), nullable=False)


class SanitySummarySchema(ma.ModelSchema):
    class Meta:
        model = SanitySummary
