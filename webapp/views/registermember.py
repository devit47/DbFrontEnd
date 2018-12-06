from flask import Blueprint, render_template, request

bp = Blueprint(__name__, __name__, template_folder='template')


@bp.route('/registermember', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('registermember'):

            memberdetails = []

            memberdetails.append(request.form.get('firstname'))
            memberdetails.append(request.form.get('surname'))
            memberdetails.append(request.form.get('dob'))
            memberdetails.append(request.form.get('phnumber'))
            memberdetails.append(request.form.get('address'))
            memberdetails.append(request.form.get('email'))
            memberdetails.append(request.form.get('password'))
            memberdetails.append(request.form.get('collegeid'))

            return memberdetails[2] + ' ' + memberdetails[7]

    return render_template('registerMember.html')
