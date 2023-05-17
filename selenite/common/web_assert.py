from typing import Optional, Any

from selene import browser

from selenite.common import predicate

DEFAULT_MSG_TRUE = 'Condition should be true'
DEFAULT_MSG_FALSE = 'Condition should be false'
DEFAULT_MSG_EQUAL = 'Actual value {actual} is not equal to expected value {expected}'
DEFAULT_MSG_NOT_EQUAL = 'Actual value {actual} should not be equal to expected value {expected}'
DEFAULT_MSG_IS_NONE = 'Object should be None'
DEFAULT_MSG_IS_NOT_NONE = 'Object should not be None'
DEFAULT_MSG_IN = 'Object {obj} should be in container {container}'
DEFAULT_MSG_NOT_IN = 'Object {obj} should not be in container {container}'


def failure_with_hook(condition: bool, msg: Optional[str] = None) -> None:
    """
    Wait for a condition to be true, and raise an AssertionError if it is not.

    Args:
        condition (bool): The condition to wait for.
        msg (Optional[str]): The message to raise if the condition is not met.

    Returns:
        None

    Example:
        >>> failure_with_hook(True, 'This should not raise an error')
        None
    """
    def fn(entity: Any):
        if not condition:
            raise AssertionError(msg)

    browser.wait.for_(fn)


def _assert_with_hook_failure():
    """
    A class for asserting conditions with a hook failure.

    Example:
        >>> predicate = _assert_with_hook_failure()
        >>> predicate.is_true(True, 'This should not raise an error')
        None
    """
    class Predicate:

        @staticmethod
        def is_true(condition: bool, msg: Optional[str] = None) -> None:
            """
            Assert that a condition is true.

            Args:
                condition (bool): The condition to assert.
                msg (Optional[str]): The message to raise if the condition is not met.

            Returns:
                None

            Example:
                >>> Predicate.is_true(True, 'This should not raise an error')
                None
            """
            return failure_with_hook(predicate.is_truthy(condition), msg or DEFAULT_MSG_TRUE)

        @staticmethod
        def is_false(condition: bool, msg: Optional[str] = None) -> None:
            """
            Assert that a condition is false.

            Args:
                condition (bool): The condition to assert.
                msg (Optional[str]): The message to raise if the condition is not met.

            Returns:
                None

            Example:
                >>> Predicate.is_false(False, 'This should not raise an error')
                None
            """
            return failure_with_hook(predicate.is_truthy(not condition), msg or DEFAULT_MSG_FALSE)

        @staticmethod
        def is_equal(actual: object, expected: object, msg: Optional[str] = None) -> None:
            """
            Assert that two objects are equal.

            Args:
                actual (object): The actual object.
                expected (object): The expected object.
                msg (Optional[str]): The message to raise if the objects are not equal.

            Returns:
                None

            Example:
                >>> Predicate.is_equal(1, 1, 'This should not raise an error')
                None
            """
            msg = msg or DEFAULT_MSG_EQUAL.format(actual=actual, expected=expected)
            return failure_with_hook(predicate.equals(expected)(actual), msg)

        @staticmethod
        def is_in(obj: object, container: object, msg: Optional[str] = None) -> None:
            """
            Assert that an object is in a container.

            Args:
                obj (object): The object to assert.
                container (object): The container to assert.
                msg (Optional[str]): The message to raise if the object is not in the container.

            Returns:
                None

            Example:
                >>> Predicate.is_in(1, [1, 2, 3], 'This should not raise an error')
                None
            """
            msg = msg or DEFAULT_MSG_IN.format(obj=obj, container=container)
            return failure_with_hook(predicate.includes(obj)(container), msg)

    return Predicate()


web_assert = _assert_with_hook_failure()
