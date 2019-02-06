"""
Initialize Flask application.
"""
from flask import Flask, render_template
from backend.api import api


class CustomFlask(Flask):
    """
    Custom Flask application to override the Jinja's tag
    to avoid conflict with Vue's tag
    """
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))


def create_app():
    """
    Create the app for flask run
    """
    app = CustomFlask(__name__, instance_relative_config=True,
                      static_folder='../../instance/dist/static',
                      template_folder='../../instance/dist')
    app.register_blueprint(api)

    @app.route('/')
    def index():
        """
        Render the vue generated html
        """
        return render_template('index.html')

    return app
