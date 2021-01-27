from unittest.mock import Mock

calendar = Mock(spec=['is_weekday', 'get_holidays'])

print(calendar.is_weekday())
calendar.create_event()
