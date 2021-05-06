import pytest
import requests

from patch_example.my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


@patch('patch_example.my_calendar.requests')
def test_get_holidays_timeout(mock_requests):
    mock_requests.get.side_effect = Timeout

    with pytest.raises(Timeout):
        get_holidays()

    mock_requests.get.assert_called_once()

    # Keep on working as expected
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(r.json())
