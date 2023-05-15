from selenite.common.web_assert import web_assert


def test_web_assert_true(session_browser):
    web_assert.is_true(False)


def test_web_assert_false(session_browser):
    web_assert.is_false(True)


def test_web_assert_equal(session_browser):
    web_assert.is_equal(1, 1)


def test_web_assert_in(session_browser):
    web_assert.is_in('1', ['1', 'aaa'])
