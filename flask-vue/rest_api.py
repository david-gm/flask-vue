from flask import (Blueprint, request, render_template, abort, jsonify)

bp = Blueprint('rest_api', __name__, template_folder='templates', url_prefix='/rest')


@bp.route('/request')
def request():
    new_person = {
        'name': 'David Gmeindl',
        'address': ['Austria', 'Graz', 'Hauptplatz 24'],
        'age': 31
    }
    return jsonify(new_person)
