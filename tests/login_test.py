from app import db

from app.db.models import User

def test_login():
    caitlin = User("caitlin@test.com", "password")
    db.session.add(caitlin)
    db.session.commit()
    caitlin = User.query.filter_by(email='cd394@njit.edu').first()
    assert caitlin.email == 'caitlin@test.com'

