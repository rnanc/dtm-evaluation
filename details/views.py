from flask import render_template
from . import details

@details.route('/details')
def detailsPage():
    return render_template('details.html')