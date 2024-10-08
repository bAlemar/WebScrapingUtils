import pytest
import requests
from unittest.mock import patch, MagicMock
from utils.requests import RequestHandler

class TestRequestHandler:

    @pytest.fixture
    def request_handler(self):
        """Fixture to create a RequestHandler instance."""
        return RequestHandler()

    @patch('requests.get')
    def test_get_success(self, mock_get, request_handler):
        """Test successful GET request."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        response = request_handler.get('http://testurl.com')

        assert response.status_code == 200
        assert response.json() == {"key": "value"}
        mock_get.assert_called_once_with('http://testurl.com', headers=request_handler.headers)

    @patch('requests.get')
    def test_get_failure(self, mock_get, request_handler):
        """Test GET request failure."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        with pytest.raises(requests.exceptions.HTTPError):
            request_handler.get('http://testurl.com')

    @patch('requests.get')
    def test_get_with_cookies_success(self, mock_get, request_handler):
        """Test successful GET request with cookies."""
        mock_response_initial = MagicMock()
        mock_response_initial.status_code = 200
        mock_response_initial.cookies = {'cookie_name': 'cookie_value'}
        mock_response_initial.raise_for_status = MagicMock()
        mock_response_final = MagicMock()
        mock_response_final.status_code = 200
        mock_response_final.raise_for_status = MagicMock()
        mock_get.side_effect = [mock_response_initial, mock_response_final]

        response = request_handler.get_with_cookies('http://testurl.com')

        assert response.status_code == 200
        mock_get.assert_any_call('http://testurl.com', headers=request_handler.headers)
        mock_get.assert_any_call('http://testurl.com', cookies=mock_response_initial.cookies, headers=request_handler.headers)

    @patch('requests.get')
    def test_get_with_cookies_failure(self, mock_get, request_handler):
        """Test GET request with cookies failure."""
        mock_response_initial = MagicMock()
        mock_response_initial.status_code = 200
        mock_response_initial.cookies = {'cookie_name': 'cookie_value'}
        mock_response_initial.raise_for_status = MagicMock()
        mock_response_final = MagicMock()
        mock_response_final.status_code = 404
        mock_response_final.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.side_effect = [mock_response_initial, mock_response_final]
