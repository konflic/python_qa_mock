import my_calendar

from unittest.mock import Mock

# Автоматически патчим те методы которые нашли в объекте
calendar = Mock(spec=my_calendar)

print(calendar.is_weekday())
print(calendar.get_holidays())
