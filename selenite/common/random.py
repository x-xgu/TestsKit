import random
import string
from typing import Union, Any


def random_int(min_value: int = 0, max_value: int = 1000) -> int:
    """
    Generate a random integer between min_value and max_value

    Args:
        min_value (int): The minimum value of the range (inclusive). Default is 0.
        max_value (int): The maximum value of the range (inclusive). Default is 1000.

    Returns:
        int: A random integer between min_value and max_value.

    Example:
        >>> random_int(1, 10)
        7
    """
    return random.randint(min_value, max_value)


def random_float(
        min_value: float = 0.0,
        max_value: float = 1.0,
        num_decimal_places: int = 2,
        to_str: bool = False
) -> Union[str, float]:
    """
    Generate a random float between min_value and max_value

    Args:
        min_value (float): The minimum value of the range (inclusive). Default is 0.0.
        max_value (float): The maximum value of the range (inclusive). Default is 1.0.
        num_decimal_places (int): The number of decimal places to round the float to. Default is 2.
        to_str (bool): Whether to return the float as a string. Default is False.

    Returns:
        Union[str, float]: A random float between min_value and max_value.

    Example:
        >>> random_float(1.0, 2.0, 3, True)
        '1.234'
    """
    def _random_float_to_str(num):
        return '{:.{dp}f}'.format(num, dp=num_decimal_places)

    value = round(random.uniform(min_value, max_value), num_decimal_places)
    if to_str:
        return _random_float_to_str(value)

    return value


def random_string(length: int = 10) -> str:
    """
    Generate a random string with the combination of lowercase and uppercase letters

    Args:
        length (int): The length of the string to generate. Default is 10.

    Returns:
        str: A random string with the combination of lowercase and uppercase letters.

    Example:
        >>> random_string(5)
        'aBcDe'
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_bool() -> bool:
    """
    Generate a random boolean value

    Returns:
        bool: A random boolean value.

    Example:
        >>> random_bool()
        True
    """
    return bool(random.getrandbits(1))


def random_choice(lst: list) -> Any:
    """
    Generate a random choice from a list

    Args:
        lst (list): The list to choose from.

    Returns:
        Any: A random choice from the list.

    Example:
        >>> random_choice([1, 2, 3, 4, 5])
        3
    """
    return random.choice(lst)


def random_chinese(length: int = 5) -> str:
    """
    Generate a random Chinese string

    Args:
        length (int): The length of the string to generate. Default is 5.

    Returns:
        str: A random Chinese string.

    Example:
        >>> random_chinese(3)
        '煮烤鸡'
    """
    return ''.join(chr(random.randint(0x4e00, 0x9fa5)) for _ in range(length))
