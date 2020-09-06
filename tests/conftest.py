"""
Conftest.py 

Write fixtures in this file so that they can be available to all the test files

example fixture

import pytest
@pytest.fixture
def supply_AA_BB_CC():
	aa=25
	bb =35
	cc=45
	return [aa,bb,cc]

other tests will take this fixture as an argument
"""