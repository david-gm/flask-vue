from flask import (Blueprint, request, render_template, abort)
from jinja2 import TemplateNotFound

bp = Blueprint('flask-vue', __name__, template_folder='templates')


@bp.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
