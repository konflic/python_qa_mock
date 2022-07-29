import pytest
import requests
import json

from mtb_example.imposters import update_add_imposter


# Change to http://localhost:8080
def pytest_addoption(parser):
    parser.addoption("--url", default="http://localhost:8080", help="Url for test api location")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def set_mock(request, base_url):

    if "localhost" in base_url:

        def wrapper(data_to_mock):
            # run with --url http://localhost:8080
            # We set imposter to mountebank
            requests.request(
                'POST',
                'http://localhost:2525/imposters',
                data=json.dumps(update_add_imposter(data_to_mock)),
                headers={"content-type": "application/json"}
            )

            def fin():
                requests.delete("http://localhost:2525/imposters/8080")

            request.addfinalizer(fin)

        return wrapper

    def stub(arg):
        pass

    return stub
