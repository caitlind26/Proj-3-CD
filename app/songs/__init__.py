import csv
import logging
from app.logging_config import configure_csv_logging
import os

from flask import Flask, Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from app.db import db
from app.db.models import Song
from app.songs.forms import upload_csv_file
from werkzeug.utils import secure_filename, redirect

songs = Blueprint('songs', __name__,
                        template_folder='templates')

upload = Blueprint('upload', __name__, template_folder='templates' )

UPLOAD_FOLDER = '/app/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@songs.route('/songs', methods=['GET'], defaults={"page": 1})
@songs.route('/songs/<int:page>', methods=['GET'])
def songs_browse(page):
    page = page
    per_page = 1000
    pagination = Song.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_songs.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)

@songs.route('/songs/upload', methods=['POST', 'GET'])
@login_required
def songs_upload():
    form = upload_csv_file()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        configure_csv_logging()
        logging.basicConfig(filename='csv.log', level= logging.INFO, format='[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s, %(levelname)s : %(message)s')
        #user = current_user
        list_of_songs = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_songs.append(Song(row['Name'],row['Artist'], row['Year'], row['Genre']))

        current_user.songs = list_of_songs
        db.session.commit()

        return redirect(url_for('songs.songs_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)