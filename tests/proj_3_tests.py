import logging

from app import db
from app.db.models import User, Song


"""Tests for Login"""

def login_test():
    caitlin = User("caitlin@test.com","password")
    db.session.add(caitlin)
    rv = self.login('caitlin','password')
    assert 'Welcome' in rv.data

"""Tests for Registration"""

def test_registration():


"""Tests for Accessing Dashboard as a Logged in User"""
    def dashboard_test(client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome" in response.data


"""Tests for Denying Access to Dashboard"""

"""Tests for Denying Access to Uploading the CSV file"""

"""Tests that the CSV file is Uploaded and Processed """

def test_csv_upload(self):
    with open ("music.csv", "w") as file:
        w = csv.writer(file)
