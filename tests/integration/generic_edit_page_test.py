from selene import browser

from tests import resources
from selenite.core.web.generic_page.edit_page import EditPage

EDIT_PAGE_URL = resources.url('orderapp/order.html')


class OrderAPP(EditPage):
    locate_function = (
        lambda _, label, following_tag:
        f'.//*[text()[normalize-space(.) = concat("", "{label}")]]/following-sibling::{following_tag}'
    )

    def open(self):
        browser.open(EDIT_PAGE_URL)


order_app = OrderAPP()


def test_input_in_edit_page(session_browser):
    order_app.open()

    order_app.select_dropdown_menu_after_label('Title:', 'Mrs')

    order_app.input_text_after_label('First name:', 'xxx')
