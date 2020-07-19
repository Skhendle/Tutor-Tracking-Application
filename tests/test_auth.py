import pytest
from flaskr import create_app

def test_max():
    val = 6
    assert val == 6

def test_min():
    val = 1
    assert val == 1
