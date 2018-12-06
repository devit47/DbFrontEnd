from flask import Blueprint, render_template, request
import webapp.models.college as db

bp = Blueprint(__name__, __name__, template_folder='template')


@bp.route('/registercollege', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('registercollege'):

            db.add_college(request.form.get('collegename'))

    return render_template('registercollege.html')
