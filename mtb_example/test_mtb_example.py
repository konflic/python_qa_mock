import cerberus
import requests
import random

AUTH_DATA = {
    "login": "admin",
    "password": "admin"
}

schema = {
    "name": {"type": "string", "required": True},
    "surname": {"type": "string", "required": True},
    "grade": {"type": "number", "required": True},
    "sex": {"type": "string", "required": True}
}


def test_update_add_authorized_session(base_url, set_mock):
    # Create session
    session = requests.Session()

    # Authorization
    session.request("login", f"{base_url}/auth/login", json=AUTH_DATA)

    # Create user
    data_to_make = {
        "name": "Test" + str(random.randint(10, 1000)),
        "surname": "TestSurname",
        "grade": 10,
        "sex": "male"
    }

    response = session.post(f"{base_url}/update/add", json=data_to_make)

    # Verify addition and response
    try:
        assert response.json().get("status") == "ok"
    except AssertionError:
        raise AssertionError(response.json())

    data = response.json().get("data")
    v = cerberus.Validator()

    assert v.validate(data, schema)
