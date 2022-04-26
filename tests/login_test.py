from app import db

from app.db.models import User

def test_login():
    caitlin = User(email="caitlin@test.com", password="password")
    db.session.add(caitlin)

