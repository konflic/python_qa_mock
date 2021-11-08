import my_calendar
from unittest.mock import create_autospec

calendar = create_autospec(my_calendar)

calendar.is_weekday()
calendar.get_holidays()
