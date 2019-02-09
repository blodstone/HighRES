from backend.model import db, ma


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    doc_id = db.Column(db.String(25), nullable=False)
    doc_json = db.Column(db.Text, nullable=False)

    # For ground truth comparison
    sanity_statement = db.Column(db.Text, nullable=True)
    sanity_answer = db.Column(db.Boolean, nullable=True, default=True)

    # For reference comparison
    sanity_statement_2 = db.Column(db.Text, nullable=True)
    sanity_answer_2 = db.Column(db.Boolean, nullable=True, default=True)

    # For checking whether doc_json is empty or not
    has_highlight = db.Column(db.Boolean, nullable=False, default=False)

    doc_statuses = db.relationship('DocStatus', backref='document', lazy=True)

    dataset_id = db.Column(db.INTEGER, db.ForeignKey('dataset.id'), nullable=True)


class DocumentSchema(ma.ModelSchema):
    class Meta:
        model = Document
