from unittest.mock import Mock

calendar = Mock(spec=['is_weekday', 'get_holidays'])

print(calendar.is_weekday())

# Этот метод не в списке и потому не пропатчен
print(calendar.get_holidays())
