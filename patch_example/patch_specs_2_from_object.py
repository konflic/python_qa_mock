import my_calendar as calendar

from unittest.mock import Mock

# Автоматически патчим те методы которые нашли в объекте
mocked = True

if mocked:
    calendar = Mock(spec=calendar)

print(calendar.is_weekday())
print(calendar.get_holidays())
