from flask_login import login_user, login_required, logout_user, current_user
import logging

from app import db
from app.db.models import User, Song

from app.auth import register

def registering_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        #check that you don't have any users or songs
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('cd394@njit.edu', 'test123')
        #add it to get ready to be committed

        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='cd394@njit.edu').first()
        #asserting that the user retrieved is correct
        assert user.email == 'cd394@njit.edu'
