from flask import Blueprint, render_template

import webapp.models.member as member_data
import webapp.models.college as college_data
import webapp.models.listing as listing_data

bp = Blueprint(__name__, __name__, template_folder='template')


@bp.route('/', methods=['POST', 'GET'])
def show():
    members = member_data.get_all_members()
    colleges = college_data.get_all_colleges()
    listings = listing_data.get_all_listings()
    return render_template('index.html', members=members, colleges=colleges, listings=listings)
