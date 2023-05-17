from __future__ import annotations

import time
from typing import List, Union, Callable, Dict

from selene import Collection, by, query, have, be, Element

from selenite import common
from selenite.common.web_assert import web_assert


class Entity:
    """
    A class representing a generic entity on a web page.
    """
    thead: Collection = None
    tbody: Collection = None
    child: str = '*'

    @property
    def ths(self) -> List[str]:
        """
        Returns a list of strings representing the text content of the table headers.
        """
        return [_.get(query.text) for _ in self.thead]

    @property
    def table_element_list(self) -> List[List[Element]]:
        """
        Returns a list of lists of elements representing the table rows and columns.
        """
        return [[_ for _ in row.all(by.xpath(self.child))] for row in self.tbody]

    @property
    def table_text_list(self) -> List[List[str]]:
        """
        Returns a list of lists of strings representing the text content of the table rows and columns.
        """
        i = self.table_element_list
        text_list = [[_.get(query.text) for _ in __] for __ in i]
        return text_list

    @property
    def table_row_size(self) -> int:
        """
        Returns the number of rows in the table.
        """
        return len(self.tbody)

    def matching_elements_in_table_by_row_keyword(self, row_keyword: Union[str, list]) -> Collection:
        """
        Returns a collection of elements that match the given row keyword(s).

        Args:
            row_keyword: A string or list of strings representing the row keyword(s) to match.

        Returns:
            A collection of elements that match the given row keyword(s).

        Example:
            >>> matching_elements_in_table_by_row_keyword('keyword')
            Collection([<Element>, <Element>, ...])
        """
        elements = self.tbody
        for keyword in ([row_keyword] if isinstance(row_keyword, str) else row_keyword):
            elements = elements.by(have.text(keyword))
            if len(elements) == 0:
                break
        return elements

    def matching_dictionaries_in_table_by_dictionary(self, dictionary: dict) -> list:
        """
        Returns a list of dictionaries representing the rows that match the given dictionary.

        Args:
            dictionary: A dictionary representing the row to match.

        Returns:
            A list of dictionaries representing the rows that match the given dictionary.

        Example:
            >>> matching_dictionaries_in_table_by_dictionary({'header1': 'value1', 'header2': 'value2'})
            [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}, ...]
        """
        return common.matching.matching_dictionaries(
            common.convert.zip_dict(self.ths, *self.table_text_list)).exact_dictionary(dictionary)

    def matching_lists_in_table_by_list(self, lst: list) -> list:
        """
        Returns a list of lists representing the rows that match the given list.

        Args:
            lst: A list representing the row to match.

        Returns:
            A list of lists representing the rows that match the given list.

        Example:
            >>> matching_lists_in_table_by_list(['value1', 'value2'])
            [['value1', 'value2'], ['value3', 'value4'], ...]
        """
        return common.matching.matching_lists(self.table_text_list).exact_list(lst)


class FormPage(Entity):
    """
    A class representing a generic form page on a web page.
    """
    def get_row_attribute_by_index(self, index: int, attribute: str) -> str:
        """
        Returns the value of the given attribute for the row at the given index.

        Args:
            index: An integer representing the index of the row.
            attribute: A string representing the attribute to retrieve.

        Returns:
            A string representing the value of the given attribute for the row at the given index.

        Example:
            >>> get_row_attribute_by_index(0, 'header1')
            'value1'
        """
        i = self.ths.index(attribute)
        text = self.tbody.element(index).all(by.xpath(self.child)).element(i).get(query.text)
        return text

    def get_row_attribute_by_text(self, row_keyword: Union[str, list], attribute) -> str:
        """
        Returns the value of the given attribute for the row that matches the given row keyword(s).

        Args:
            row_keyword: A string or list of strings representing the row keyword(s) to match.
            attribute: A string representing the attribute to retrieve.

        Returns:
            A string representing the value of the given attribute for the row that matches the given row keyword(s).

        Example:
            >>> get_row_attribute_by_text('keyword', 'header1')
            'value1'
        """
        i = self.ths.index(attribute)
        elements = self.matching_elements_in_table_by_row_keyword(row_keyword)
        text = (
            elements.element_by(be.visible).all(by.xpath(self.child)).element(i).get(query.text)
        ) if len(elements) else None
        return text

    def should_contain_sub_dictionary(self, dictionary: dict) -> FormPage:
        """
        Asserts that the table contains the given dictionary.

        Args:
            dictionary: A dictionary representing the row to match.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_contain_sub_dictionary({'header1': 'value1', 'header2': 'value2'})
            FormPage(...)
        """
        web_assert.is_true(bool(self.matching_dictionaries_in_table_by_dictionary(dictionary)))
        return self

    def should_not_contain_sub_dictionary(self, dictionary: dict) -> FormPage:
        """
        Asserts that the table does not contain the given dictionary.

        Args:
            dictionary: A dictionary representing the row to match.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_not_contain_sub_dictionary({'header1': 'value1', 'header2': 'value2'})
            FormPage(...)
        """
        web_assert.is_false(self.matching_dictionaries_in_table_by_dictionary(dictionary))
        return self

    def should_contain_sub_list(self, lst: list) -> FormPage:
        """
        Asserts that the table contains the given list.

        Args:
            lst: A list representing the row to match.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_contain_sub_list(['value1', 'value2'])
            FormPage(...)
        """
        web_assert.is_true(bool(self.matching_lists_in_table_by_list(lst)))
        return self

    def should_have_text(self, text: str) -> FormPage:
        """
        Asserts that the table contains the given text.

        Args:
            text: A string representing the text to match.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_have_text('text')
            FormPage(...)
        """
        self.tbody.by(have.text(text)).should(have.size_greater_than_or_equal(1))
        return self

    def should_have_text_by_index(self, index: int, text: str) -> FormPage:
        """
        Asserts that the row at the given index contains the given text.

        Args:
            index: An integer representing the index of the row.
            text: A string representing the text to match.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_have_text_by_index(0, 'text')
            FormPage(...)
        """
        self.tbody.element(index).should(have.text(text))
        return self

    def should_have_row_attribute(self, row_keyword: Union[str, list], attribute: str, value: str) -> FormPage:
        """
        Asserts that the row that matches the given row keyword(s) has the given attribute value.

        Args:
            row_keyword: A string or list of strings representing the row keyword(s) to match.
            attribute: A string representing the attribute to retrieve.
            value: A string representing the expected value of the attribute.

        Returns:
            The current FormPage instance.

        Example:
            >>> should_have_row_attribute('keyword', 'header1', 'value1')
            FormPage(...)
        """
        text = self.get_row_attribute_by_text(row_keyword, attribute)
        web_assert.is_equal(text, value)
        return self


class FormsPage(FormPage):
    """
    A class representing a generic forms page on a web page.
    """
    check_next_page_enable_function: Callable = None

    next_page_button: Element = None
    page_index_button: Collection = None

    def with_traverse_all_pages(self, fn: Callable, *args, **kwargs):
        """
        Calls the given function with the given arguments for each page of the table.

        Args:
            fn: A function to call for each page of the table.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            The result of the last call to the function.

        Example:
            >>> with_traverse_all_pages(lambda val: val.extend(self.table_text_list), all_info)
            [['value1', 'value2'], ['value3', 'value4'], ...]
        """
        while True:
            res = fn(*args, **kwargs)
            if not self.check_and_click_next_page_button():
                break
        return res

    def check_and_click_next_page_button(self) -> bool:
        """
        Clicks the next page button if it is enabled.

        Returns:
            A boolean indicating whether the next page button was enabled.

        Example:
            >>> check_and_click_next_page_button()
            True
        """
        enabled = not self.check_next_page_enable_function(self.next_page_button)
        self.next_page_button.click() if enabled else ...
        time.sleep(0.5)
        return enabled

    def back_to_first_page(self) -> FormsPage:
        """
        Clicks the button to return to the first page of the table.

        Returns:
            The current FormsPage instance.

        Example:
            >>> back_to_first_page()
            FormsPage(...)
        """
        self.page_index_button.by(have.text('1')).element_by(be.clickable).click()
        time.sleep(0.5)
        return self

    def matching_elements_in_tables_by_row_keyword(self, row_keyword: Union[str, list]) -> Collection:
        """
        Returns a collection of elements that match the given row keyword(s) across all pages of the table.

        Args:
            row_keyword: A string or list of strings representing the row keyword(s) to match.

        Returns:
            A collection of elements that match the given row keyword(s) across all pages of the table.

        Example:
            >>> matching_elements_in_table_by_row_keyword('keyword')
            Collection([<Element>, <Element>, ...])
        """
        while True:
            elements = self.matching_elements_in_table_by_row_keyword(row_keyword)
            if len(elements) > 0:
                break
            if not self.check_and_click_next_page_button():
                break
        return elements

    def get_table_all_info_with_dictionaries(self) -> List[Dict]:
        """
        Returns a list of dictionaries representing all rows of the table.

        Returns:
            A list of dictionaries representing all rows of the table.

        Example:
            >>> get_table_all_info_with_dictionaries()
            [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}, ...]
        """
        all_info = []
        self.with_traverse_all_pages(
            lambda val: val.extend(self.table_text_list),
            all_info
        )
        return common.convert.zip_dict(self.ths, *all_info)

    def get_table_all_info_with_lists(self) -> List[List]:
        """
        Returns a list of lists representing all rows of the table.

        Returns:
            A list of lists representing all rows of the table.

        Example:
            >>> get_table_all_info_with_lists()
            [['value1', 'value2'], ['value3', 'value4'], ...]
        """
        all_info = []
        self.with_traverse_all_pages(
            lambda val: val.extend(self.table_text_list),
            all_info
        )
        return all_info

    def matching_dictionaries_in_table_by_dictionaries(
            self,
            origin_dictionaries: List[Dict],
            dictionaries: List[Dict],
            /
    ) -> List[Dict]:
        """
        Returns a list of dictionaries that match the given dictionaries across all pages of the table.

        Args:
            origin_dictionaries: A list of dictionaries representing all rows of the table.
            dictionaries: A list of dictionaries to match.

        Returns:
            A list of dictionaries that match the given dictionaries across all pages of the table.

        Example:
            >>> matching_dictionaries_in_table_by_dictionaries(
            ...     [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}, ...],
            ...     [{'header1': 'value1'}, {'header1': 'value3'}]
            ... )
            [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]
        """
        matched_list = []
        for dictionary in dictionaries:
            tmp = common.matching.matching_dictionaries(origin_dictionaries).exact_dictionary(dictionary)
            matched_list.extend(tmp) if tmp else ...
        return matched_list

    def matching_lists_in_table_by_lists(
            self,
            origin_lists: List[List],
            lists: List[List],
            /
    ) -> List[List]:
        """
        Returns a list of lists that match the given lists across all pages of the table.

        Args:
            origin_lists: A list of lists representing all rows of the table.
            lists: A list of lists to match.

        Returns:
            A list of lists that match the given lists across all pages of the table.

        Example:
            >>> matching_lists_in_table_by_lists(
            ...     [['value1', 'value2'], ['value3', 'value4'], ...],
            ...     [['value1'], ['value3']]
            ... )
            [['value1', 'value2'], ['value3', 'value4']]
        """
        matched_list = []
        for lst in lists:
            tmp = common.matching.matching_lists(origin_lists).exact_list(lst)
            matched_list.extend(tmp) if tmp else ...
        return matched_list

    def should_contain_sub_dictionaries(self, dictionaries: List[Dict]) -> List:
        """
        Checks that the table contains the given dictionaries.

        Args:
            dictionaries: A list of dictionaries to match.

        Returns:
            A list of dictionaries that match the given dictionaries across all pages of the table.

        Example:
            >>> should_contain_sub_dictionaries(
            ...     [{'header1': 'value1'}, {'header1': 'value3'}]
            ... )
            [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]
        """
        matched_list = self.matching_dictionaries_in_table_by_dictionaries(
            self.get_table_all_info_with_dictionaries(),
            dictionaries
        )
        web_assert.is_equal(
            len(dictionaries),
            len(matched_list)
        )
        return matched_list

    def should_contain_sub_lists(self, lists: List[List]) -> List:
        """
        Checks that the table contains the given lists.

        Args:
            lists: A list of lists to match.

        Returns:
            A list of lists that match the given lists across all pages of the table.

        Example:
            >>> should_contain_sub_lists(
            ...     [['value1'], ['value3']]
            ... )
            [['value1', 'value2'], ['value3', 'value4']]
        """
        matched_list = self.matching_lists_in_table_by_lists(
            self.get_table_all_info_with_lists(),
            lists
        )
        web_assert.is_equal(
            len(lists),
            len(matched_list)
        )
        return matched_list
