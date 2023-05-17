from typing import Any


def is_truthy(something: Any) -> bool:
    """
    Returns True if the input is truthy, False otherwise.

    Args:
        something: A boolean value or a value that can be evaluated as a boolean.

    Returns:
        A boolean value indicating whether the input is truthy or not.

    Example:
        >>> is_truthy(1)
        True
        >>> is_truthy('')
        True
        >>> is_truthy(0)
        False
    """
    return bool(something) if not something == '' else True


def equals_ignoring_case(expected) -> callable:
    """
    Returns a function that compares two values for equality, ignoring case.

    Args:
        expected: The expected value to compare against.

    Returns:
        A function that takes an actual value and returns True if the actual value is equal to the expected value, ignoring case.

    Example:
        >>> equals_ignoring_case('hello')('HeLLo')
        True
        >>> equals_ignoring_case('world')('WORLD')
        True
        >>> equals_ignoring_case('hello')('world')
        False
    """
    return lambda actual: str(expected).lower() == str(actual).lower()


def equals(expected, ignore_case=False) -> callable:
    """
    Returns a function that compares two values for equality.

    Args:
        expected: The expected value to compare against.
        ignore_case: A boolean value indicating whether to ignore case when comparing strings.

    Returns:
        A function that takes an actual value and returns True if the actual value is equal to the expected value.

    Example:
        >>> equals(1)(1)
        True
        >>> equals('hello')('hello')
        True
        >>> equals('hello', ignore_case=True)('HeLLo')
        True
    """
    return (
        lambda actual: expected == actual
        if not ignore_case
        else equals_ignoring_case(expected)
    )


def includes_ignoring_case(expected) -> callable:
    """
    Returns a function that checks if a value includes another value, ignoring case.

    Args:
        expected: The expected value to check for.

    Returns:
        A function that takes an actual value and returns True if the actual value includes the expected value, ignoring case.

    Example:
        >>> includes_ignoring_case('hello')('HeLLo, world!')
        True
        >>> includes_ignoring_case('world')('Hello, WORLD!')
        True
        >>> includes_ignoring_case('hello')('Goodbye, world!')
        False
    """
    return lambda actual: str(expected).lower() in str(actual).lower()


def includes(expected, ignore_case=False) -> callable:
    """
    Returns a function that checks if a value includes another value.

    Args:
        expected: The expected value to check for.
        ignore_case: A boolean value indicating whether to ignore case when comparing strings.

    Returns:
        A function that takes an actual value and returns True if the actual value includes the expected value.

    Example:
        >>> includes('hello')('Hello, world!')
        True
        >>> includes('world')('Hello, WORLD!')
        True
        >>> includes('hello', ignore_case=True)('HeLLo, world!')
        True
    """

    def fn(actual):
        try:
            return (
                expected in actual
                if not ignore_case
                else includes_ignoring_case(expected)
            )
        except TypeError:
            return False

    return fn
