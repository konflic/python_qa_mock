from unittest.mock import Mock

mock = Mock(name='Real Python Mock')

mock = Mock(return_value=True)
mock()


mock = Mock(name='Real Python Mock')
print(mock.name)

mock = Mock()
mock.name = 'Real Python Mock'
print(mock.name)
