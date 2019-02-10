from backend.model import db, ma


class ProjectStatus(db.Model):
    __tablename__ = 'project_status'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    total_exp_results = db.Column(db.Integer, nullable=False)

    # Used in informativeness and fluency project
    summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=True)
    # ref_summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=True)

    # Used in annotation project
    # doc_id = db.Column(db.INTEGER, db.ForeignKey('document.id'), nullable=True)

    eval_proj_id = db.Column(db.INTEGER, db.ForeignKey('informativeness_project.id'), nullable=True)
    # ann_proj_id = db.Column(db.INTEGER, db.ForeignKey('annotation_project.id'), nullable=True)


class ProjectStatusSchema(ma.ModelSchema):
    class Meta:
        model = ProjectStatus


