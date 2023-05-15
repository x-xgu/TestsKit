from typing import List, Dict

import cv2
import numpy as np


def zip_dict(keys: List[str], *values) -> List[Dict]:
    """
    Merge keys and values into a list of dictionaries
    """
    dict_list = []
    [dict_list.append(dict(zip(keys, value))) for value in values]
    return dict_list


def format_decimal_number_with_commas(number):
    """
    Format decimal number with commas
    """
    formatted_number = f'{float(number):,}'
    return formatted_number


def bytes_to_numpy(bytes_data: bytes):
    """
    Convert bytes to numpy
    """
    nparr = np.frombuffer(bytes_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)


def convert_sec_to_ms(timeout):
    """
    Convert seconds to milliseconds
    """
    return timeout * 1000
