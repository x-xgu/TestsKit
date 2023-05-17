from __future__ import annotations

from typing import Callable

from selene import be, Collection, have, query, Element
from selene.support.shared.jquery_style import ss
from selenium.webdriver.support.select import Select


class LocatorConfig:
    locate_function: Callable = None

    def behind_label(self, label_value: str) -> Element:
        """
        Find the element behind the label with the given value.

        Args:
            label_value: The value of the label.

        Returns:
            The element behind the label.

        Example:
            >>> locator = LocatorConfig()
            >>> locator.locate_function = ss
            >>> locator.tag = 'input'
            >>> locator.behind_label('Username')
            Collection object
        """
        return self.s_behind_label(label_value).element_by(be.enabled)

    def s_behind_label(self, label_value: str) -> Collection:
        """
        Find the collection behind the label with the given value.

        Args:
            label_value: The value of the label.

        Returns:
            The collection behind the label.

        Example:
            >>> locator = LocatorConfig()
            >>> locator.locate_function = ss
            >>> locator.tag = 'input'
            >>> locator.s_behind_label('Username')
            Collection object
        """
        return self.locate_function(label_value, self.tag)

    def __getattr__(self, tag: str) -> LocatorConfig:
        self.tag = tag
        return self


class EditPage(LocatorConfig):
    select_option: Collection = None

    def input_text_after_label(self, label: str, text: str) -> EditPage:
        """
        Input text after the label with the given value.

        Args:
            label: The value of the label.
            text: The text to input.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'input'
            >>> edit_page.input_text_after_label('Username', 'John')
            EditPage object
        """
        self.input.behind_label(label).click().clear().type(text)
        return self

    def input_long_text_after_label(self, label: str, long_text: str) -> EditPage:
        """
        Input long text after the label with the given value.

        Args:
            label: The value of the label.
            long_text: The long text to input.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'textarea'
            >>> edit_page.input_long_text_after_label('Description', 'This is a long text.')
            EditPage object
        """
        self.textarea.behind_label(label).click().clear().type(long_text)
        return self

    def click_checkbox_after_label(self, label: str) -> EditPage:
        """
        Click the checkbox after the label with the given value.

        Args:
            label: The value of the label.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'input'
            >>> edit_page.click_checkbox_after_label('Agree')
            EditPage object
        """
        self.input.behind_label(label).click()
        return self

    def input_text_after_label_and_select_self(self, label: str, text: str) -> EditPage:
        """
        Input text after the label with the given value and select the option with the same text.

        Args:
            label: The value of the label.
            text: The text to input and select.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'input'
            >>> edit_page.select_option = ss('option')
            >>> edit_page.input_text_after_label_and_select_self('Country', 'USA')
            EditPage object
        """
        self.input_text_after_label(label, text)
        self.select_option.by(have.text(text)).element_by(be.clickable).click()
        return self

    def input_text_after_label_and_select_option(self, label: str, text: str, option: str) -> EditPage:
        """
        Input text after the label with the given value and select the option with the given value.

        Args:
            label: The value of the label.
            text: The text to input.
            option: The value of the option to select.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'input'
            >>> edit_page.select_option = ss('option')
            >>> edit_page.input_text_after_label_and_select_option('Country', 'USA', 'United States')
            EditPage object
        """
        self.input_text_after_label(label, text)
        self.select_option.by(have.text(option)).element_by(be.clickable).click()
        return self

    def click_input_box_after_label_and_select_option(self, label: str, option: str) -> EditPage:
        """
        Click the input box after the label with the given value and select the option with the given value.

        Args:
            label: The value of the label.
            option: The value of the option to select.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'input'
            >>> edit_page.select_option = ss('option')
            >>> edit_page.click_input_box_after_label_and_select_option('Country', 'United States')
            EditPage object
        """
        self.input.behind_label(label).click()
        self.select_option.by(have.text(option)).element_by(be.clickable).click()
        return self

    def click_button_after_label(self, label: str) -> EditPage:
        """
        Click the button after the label with the given value.

        Args:
            label: The value of the label.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'button'
            >>> edit_page.click_button_after_label('Submit')
            EditPage object
        """
        self.button.behind_label(label).click()
        return self

    def select_dropdown_menu_after_label(self, label: str, option: str) -> EditPage:
        """
        Select the option from the dropdown menu after the label with the given value.

        Args:
            label: The value of the label.
            option: The value of the option to select.

        Returns:
            The EditPage object.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'select'
            >>> edit_page.select_dropdown_menu_after_label('Country', 'United States')
            EditPage object
        """
        Select(self.select.behind_label(label).locate()).select_by_visible_text(option)
        return self

    def get_text_after_label(self, label: str) -> str:
        """
        Get the text after the label with the given value.

        Args:
            label: The value of the label.

        Returns:
            The text after the label.

        Example:
            >>> edit_page = EditPage()
            >>> edit_page.locate_function = ss
            >>> edit_page.tag = 'span'
            >>> edit_page.get_text_after_label('Username')
            'John'
        """
        text = self.span.behind_label(label).get(query.text)
        return text
