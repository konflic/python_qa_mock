from datetime import datetime


def is_weekend():
    """This works on weekday, but not on weekend"""
    return (5 <= datetime.today().weekday() <= 6)


import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)
sunday = datetime.datetime(year=2019, month=1, day=5)


def is_weekend():
    print("Checking date")
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (5 <= today.weekday() <= 6)


# Mock datetime to control today's date
datetime = Mock()

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = sunday
assert is_weekend()

# Mock .today() to return Saturday
datetime.datetime.today.return_value = tuesday
assert not is_weekend()
