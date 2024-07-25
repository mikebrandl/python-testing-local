import pytest
from python.app.services.database import Database
import unittest.mock as mock


@mock.patch('python.app.services.database.Database.get_users')
def test_get_user_from_database(mock_get_users):
    mock_get_users.return_value = [
        'mike',
        'jodie'
    ]
    users = Database.get_users()
    assert users == ['mike', 'jodie']
