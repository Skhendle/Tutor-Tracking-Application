import os
import tempfile

import pytest

from app import tutortracker


@pytest.fixture
def client():
    db_fd, tutortracker.app.config['DATABASE'] = tempfile.mkstemp()
    tutortracker.app.config['TESTING'] = True

    with tutortracker.app.test_client() as client:
        with tutortracker.app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(tutortracker.app.config['DATABASE'])
