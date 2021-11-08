from unittest.mock import Mock

calendar = Mock(spec=['is_weekday', 'get_holidays'])

print(calendar.is_weekday())
print(calendar.get_holidays())
