from AudioFile import db,app, route
import pytest

def test_before_any_test():
    db.drop_all()
    db.create_all()
