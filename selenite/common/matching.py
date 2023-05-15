from __future__ import annotations

import re
from typing import List, Dict


def matching_dictionaries(dictionaries: List[Dict]):
    """
    Matching dictionaries
    """
    class Matching:

        def __init__(self, dictionaries):
            self._dictionaries = dictionaries

        def exact_dictionary(self, exact_dictionary: Dict):
            """
            Exact dictionary
            """
            return [
                d
                for d in self._dictionaries
                if all(
                    d.get(key) == value
                    for key, value
                    in exact_dictionary.items()
                )
            ]

        def partial_dictionary(self, partial_dictionary: Dict):
            """
            Partial dictionary
            """
            patterns = {
                key: re.compile(pattern)
                for key, pattern
                in partial_dictionary.items()
            }
            return [
                d
                for d in self._dictionaries
                if all(
                    patterns[key].search(d[key])
                    for key
                    in partial_dictionary
                )
            ]

    return Matching(dictionaries)


def matching_lists(lists: List[List]):
    """
    Matching lists
    """
    class Matching:

        def __init__(self, lists):
            self._lists = lists

        def exact_list(self, exact_list: List):
            """
            Exact list
            """
            return [
                l_
                for l_
                in self._lists
                if all(
                    item in l_
                    for item
                    in exact_list
                )
            ]

        def partial_list(self, partial_list: List):
            """
            Partial list
            """
            regex_list = [
                re.compile(pattern)
                if isinstance(pattern, str)
                else pattern
                for pattern
                in partial_list
            ]
            return [
                l_
                for l_
                in self._lists
                if all(
                    regex.search(str(elem))
                    for regex, elem
                    in zip(regex_list, l_)
                )
            ]

    return Matching(lists)
