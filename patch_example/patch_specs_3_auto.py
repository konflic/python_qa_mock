import my_calendar as calendar

from unittest.mock import create_autospec

calendar = create_autospec(calendar)

calendar.is_weekday()
calendar.get_holidays()
