import requests

from unittest.mock import Mock


# Mock requests to control its behavior

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


def log_request(url):
    # Log a fake request for test output purposes
    print(f'Making a request to {url}.')

    # Create a new Mock to imitate a Response
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '12/31': 'New Year',
    }

    return response_mock


requests = Mock()


def test_get_holidays_logging():
    # Test a successful, logged request
    requests.get.side_effect = log_request
    response = get_holidays()
    assert response['12/31'] == 'New Year'
    assert response['12/25'] == 'Christmas'
