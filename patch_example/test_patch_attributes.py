import pytest

from patch_example.my_calendar import requests, get_holidays
from unittest.mock import patch


@patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
def test_get_holidays_timeout(mock_placeholder):

    with pytest.raises(requests.exceptions.Timeout):
        get_holidays()

    # Keep on working as expected
    r = requests.post("https://jsonplaceholder.typicode.com/posts")
    print(r.json())
