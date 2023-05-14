def test_base_url_setting(base_url):
    assert base_url == 'https://www.google.com'


def test_timeout_setting(timeout):
    assert timeout == 10
