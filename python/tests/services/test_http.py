import pytest
import unittest.mock as mock

import requests

from python.app.services.jsonplaceholder import JsonPlaceholder


@mock.patch('requests.get')
def test_get_user_from_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = ['mike','jodie']
    mock_get.return_value = mock_response

    users = JsonPlaceholder.get_users()
    assert users == ['mike', 'jodie']

@mock.patch('requests.get')
def mock_error_response(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        JsonPlaceholder.get_users()

