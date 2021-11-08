import pytest

from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

requests = Mock()


def test_get_holidays_retry():
    # Create a new Mock to imitate a Response
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independence Day',
    }

    # Set the side effect of .get()
    requests.get.side_effect = [Timeout, response_mock]

    # Test that the first request raises a Timeout
    with pytest.raises(Timeout):
        get_holidays()

    # Now retry, expecting a successful response
    assert get_holidays()['12/25'] == 'Christmas'

    # Finally, assert .get() was called twice
    assert requests.get.call_count == 2
