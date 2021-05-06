from unittest.mock import Mock

mock = Mock(return_value=True)

if mock():
    print("Return value is True")
else:
    print("Return value is False")

# Set name for Mock object
mock = Mock(name='Мой собственный мок')
print(mock.name)

# Set regular attribute to Mock
mock = Mock()
mock.name = 'Имя добавлено через атрибут'
print(mock.name)

# Old fashion
response_mock = Mock()
response_mock.json.return_value = {'12/25': 'Christmas', '7/4': 'Independence Day', }

# New label
response = Mock(**{'json.return_value': {'12/25': 'Christmas', '7/4': 'Independence Day'}})

print(response.json())
