from typing import List, Dict

import cv2
import numpy as np


def zip_dict(keys: List[str], *values: List) -> List[Dict[str, str]]:
    """
    Merge keys and values into a list of dictionaries

    Args:
        keys (List[str]): A list of strings representing the keys for the dictionaries
        *values (List): A variable number of arguments representing the values for the dictionaries

    Returns:
        List[Dict[str, List]]: A list of dictionaries with the keys and values merged together

    Example:
        >>> zip_dict(['name', 'age'], ['John', 25], ['Jane', 30])
        [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]
    """
    dict_list = []
    [dict_list.append(dict(zip(keys, value))) for value in values]
    return dict_list


def format_decimal_number_with_commas(number: float) -> str:
    """
    Format decimal number with commas

    Args:
        number (float): A decimal number to be formatted with commas

    Returns:
        str: A string representation of the formatted decimal number

    Example:
        >>> format_decimal_number_with_commas(1234567.89)
        '1,234,567.89'
    """
    formatted_number = f'{float(number):,}'
    return formatted_number


def bytes_to_numpy(bytes_data: bytes) -> np.ndarray:
    """
    Convert bytes to numpy

    Args:
        bytes_data (bytes): A bytes object to be converted to a numpy array

    Returns:
        np.ndarray: A numpy array representing the image data

    Example:
        >>> with open('image.jpg', 'rb') as f:
        ...     image_bytes = f.read()
        ...
        >>> image_data = bytes_to_numpy(image_bytes)
    """
    nparr = np.frombuffer(bytes_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)


def convert_sec_to_ms(timeout: float) -> float:
    """
    Convert seconds to milliseconds

    Args:
        timeout (float): A timeout value in seconds

    Returns:
        float: The timeout value converted to milliseconds

    Example:
        >>> convert_sec_to_ms(2.5)
        2500.0
    """
    return timeout * 1000
