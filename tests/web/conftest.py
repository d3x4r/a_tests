import pytest
from selenium import webdriver

browser_list = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    normalized_name = browser_name.lower()

    if normalized_name not in browser_list.keys():
        raise BaseException('wrong browser')

    browser = browser_list[normalized_name]()

    yield browser

    browser.quit()
