import pytest

from patch_example.my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


def test_get_holidays_timeout():

    with patch('patch_example.my_calendar.requests') as mock_requests:
        mock_requests.get.side_effect = Timeout

        with pytest.raises(Timeout):
            get_holidays()

        mock_requests.get.assert_called_once()
