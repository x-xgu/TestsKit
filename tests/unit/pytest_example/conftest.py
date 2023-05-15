import pytest

from selenite.conf.pytest.options import Option


class MyOption:

    def __init__(self, request):
        self.request = request

    @Option.default('https://www.google.com')
    def base_url(self):
        pass

    @Option.default(10)
    def timeout(self):
        pass


def pytest_addoption(parser):
    Option.register_all(from_cls=MyOption, in_parser=parser)


@pytest.fixture
def config(request):
    return MyOption(request)


@pytest.fixture
def base_url(config):
    return config.base_url


@pytest.fixture
def timeout(config):
    return config.timeout
