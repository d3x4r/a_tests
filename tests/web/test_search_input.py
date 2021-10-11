from actions.mediator import Mediator
from actions.base_actions import BaseActions


def test_search_input(browser):
    LINK = 'http://ya.ru'
    SEARCH_TEXT = 'texttexts'
    Firefox = BaseActions(Mediator(), browser)
    Firefox.open(LINK)
    Firefox.is_search_input_enabled()
    Firefox.write_search_text(SEARCH_TEXT)
    Firefox.is_search_submit_button_enabled()
