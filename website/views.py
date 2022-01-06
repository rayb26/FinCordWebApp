from flask import Blueprint, render_template, request, flash

from website import Database

views = Blueprint('views', __name__)


@views.route('/view-data', methods=['GET'])
def view_data():
    # terms = Database.read_data().get('terms')
    # definitions = Database.read_data().get('definitions')
    return render_template('view-data.html', terms=Database.read_data())


@views.route('/add-term', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
def add_term():
    data = request.form

    print(data)
    if request.method == 'POST' and len(data.get('term')) > 0 and len(data.get('definition')) > 0:
        Database.add_term_def(data.get('term'), data.get('definition'))
        flash("Term Added", category='success')
        print("Added")

    return render_template('add-term.html')
