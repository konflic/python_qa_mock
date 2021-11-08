from unittest.mock import patch
from my_calendar import is_weekday

print(is_weekday())

with patch('__main__.is_weekday'):
    print(is_weekday())

print(is_weekday())