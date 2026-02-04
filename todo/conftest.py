import pytest
import toml
import os
from django.contrib.auth.models import User
from django.test import Client

@pytest.fixture(scope='session')
def config():
    CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config_runner.toml')
    return toml.load(CONFIG_PATH)

def get_unique_username(base, suffix):
    return f"{base}_{suffix}"

@pytest.fixture(scope='session')
def test_username(config):
    return config['test_user']['username']

@pytest.fixture(scope='session')
def test_password(config):
    return config['test_user']['password']

@pytest.fixture(scope='session')
def new_user_username(config):
    return config['new_user']['username']

@pytest.fixture(scope='session')
def new_user_password(config):
    return config['new_user']['password']

@pytest.fixture
def test_user(db, config):
    username = get_unique_username(config['test_user']['username'], 'fixture')
    password = config['test_user']['password']
    user = User.objects.create_user(username=username, password=password)
    return {'username': username, 'password': password, 'user': user}

@pytest.fixture
def new_user(db, config):
    username = get_unique_username(config['new_user']['username'], 'fixture')
    password = config['new_user']['password']
    user = User.objects.create_user(username=username, password=password)
    return {'username': username, 'password': password, 'user': user}

@pytest.fixture
def authenticated_client(test_user):
    client = Client()
    client.login(username=test_user['username'], password=test_user['password'])
    return client
