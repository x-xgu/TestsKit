from selene import browser, have
from selene.support.shared.jquery_style import ss, s

from testskit.core.web.generic_page.form_page import FormsPage


class Page(FormsPage):
    thead = ss('//div[contains(@ng-show, "tabValue") and not(contains(@class, "ng-hide"))]//thead//th')
    tbody = ss('//div[contains(@ng-show, "tabValue") and not(contains(@class, "ng-hide"))]//tbody//tr')
    check_next_page_enable_function = (lambda _, val: val.matching(have.attribute('class').value_containing('is-disabled')))
    next_page_button = s('//ul[@class="ag-pagination__inner"]//li[@ng-click="vm.nextPage()"]')
    page_index_button = ss('//ul[@class="ag-pagination__inner"]/li[contains(@class, "ag-pagination--pager")]')

    def open(self):
        browser.open('https://192.168.15.64/login.jsp#/ds/submc_statistics_report_analysis_action/list/1')


page = Page()


def test_read_form(session_browser):
    page.open()
    # breakpoint()
    print(page.get_table_all_info_with_dictionaries())

    