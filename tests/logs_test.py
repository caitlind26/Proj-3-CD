import logging
from logging import config
from pathlib import Path

"""Tests debug file"""
def test_debug_file():
   file_name = Path(__file__)
   test_dir = file_name.parent
   proj_dir = test_dir.parent
   app_dir = proj_dir / "app"
   log_dir = app_dir / "logs"
   debug_file = log_dir / "debug.log"
   assert debug_file.exists()

"""Tests request log file is created"""
def test_request_log_file():
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    request_file = log_dir / "request.log"
    assert request_file.exists()