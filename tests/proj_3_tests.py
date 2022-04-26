import logging

from app import db
from app.db.models import User, Song

"""Tests for Login"""

def login_test():
    caitlin = User( email = "caitlin@test.com", password = "password")
    db.session.add(caitlin)
    rv = self.login('caitlin','password')
    assert 'Welcome' in rv.data

"""Tests for Registration"""

def test_registration():


"""Tests for Accessing Dashboard as a Logged in User"""
    def dashboard_test():

"""Tests for Denying Access to Dashboard"""

"""Tests for Denying Access to Uploading the CSV file"""

"""Tests that the CSV file is Uploaded and Processed """