import my_calendar

from unittest.mock import Mock

calendar = Mock(spec=my_calendar)

print(calendar.is_weekday())

calendar.create_event()