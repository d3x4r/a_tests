from actions.browser_actions import BrowserActions


def test_search_input(browser):
    LINK = 'http://ya.ru'
    app = BrowserActions.connect(browser, 5)
    SEARCH_TEXT = 'texttext'
    app.open(LINK)
    app.is_search_input_enabled()
    app.write_search_text(SEARCH_TEXT)
    app.is_search_submit_button_enabled()
