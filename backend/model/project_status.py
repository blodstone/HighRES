from backend.model import db, ma
from backend.model.result import FluencyResult


class ProjectStatus(db.Model):
    __tablename__ = 'project_status'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)

    # total_exp_results = db.Column(db.Integer, nullable=False, default=1)
    # total_results = db.Column(db.Integer, nullable=False, default=0)

    is_finished = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    validity = db.Column(db.Boolean, nullable=True, default=False)
    mturk_code = db.Column(db.String(255), nullable=True)

    best_summ_score = db.Column(db.INTEGER, nullable=True)
    mediocre_summ_score = db.Column(db.INTEGER, nullable=True)
    worst_summ_score = db.Column(db.INTEGER, nullable=True)


    expired_in = db.Column(db.DateTime, nullable=True)
    # Used in informativeness and fluency project
    # summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=True)
    # ref_summary_id = db.Column(db.INTEGER, db.ForeignKey('summary.id'), nullable=True)

    # Used in annotation project
    # doc_id = db.Column(db.INTEGER, db.ForeignKey('document.id'), nullable=True)

    eval_proj_id = db.Column(db.INTEGER, db.ForeignKey('evaluation_project.id'), nullable=True)
    fluency_proj_id = db.Column(db.INTEGER, db.ForeignKey('fluency_project.id'), nullable=True)
    sanity_summ_id = db.Column(db.INTEGER, db.ForeignKey('sanity_summary.id'), nullable=True)
    results = db.relationship('FluencyResult', cascade='delete')
    # ann_proj_id = db.Column(db.INTEGER, db.ForeignKey('annotation_project.id'), nullable=True)


class ProjectStatusSchema(ma.ModelSchema):
    class Meta:
        model = ProjectStatus


