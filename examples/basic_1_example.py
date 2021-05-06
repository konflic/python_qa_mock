import json
from unittest.mock import Mock

mock = Mock()

print(mock)

print("\n=== Mock creates its properties when you access them ===")
print(mock.some_attribute)
print(mock.do_something())

print("\n=== Mock example for json library ===")
json = Mock()
print(json)

# 1. This method is also a mock, and can accept any amount of arguments.
print(json.dumps())
print(json.dumps("hello"))
print(json.dumps("hello", 1, 2, 3, 4, None))

# 2. This method also returns Mock object
json.dumps("hello").get("test").get(None)

print("\n=== Mock example asserting mock calls ===")
# 3. You can check how loads was called
json.dumps.assert_called()

# json.dumps.assert_called_once() - Only if method was called once
json.dumps.assert_called_with('hello')
json.loads("test_once")
json.loads.assert_called_once_with('test_once')
