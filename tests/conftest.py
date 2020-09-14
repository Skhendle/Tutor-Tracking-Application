from app import create_app
import pytest
from config import Config

@pytest.fixture
def flask_app_client():
	app = create_app(config_class=Config)
	client = app.test_client()
		
	return client


