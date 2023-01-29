import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def sample_inputs():
    inputs = {
        'price' :1000000,
        'down_payment' : 200000,
        'rate' : 5,
        'amortization' : 25,
        'payment_schedule' : 'monthly'
    }
    return inputs