import pytest
import requests
import json

from mtb_example.imposters import update_add_imposter


def pytest_addoption(parser):
    parser.addoption("--url", default="https://my-api-examaple.herokuapp.com/api", help="Url for test api location")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def set_mock(base_url):
    if "localhost" in base_url:

        # We set imposter to mountebank
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(update_add_imposter),
            headers={"content-type": "application/json"}
        )
