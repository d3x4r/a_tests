from actions.base_actions import BaseActions
from actions.mediator import Mediator


def test_search_input(app):
    APP_PATH = r'C:\Program Files\Notepad++\notepad++.exe'
    Notepad = BaseActions(Mediator(), app)
    Notepad.open(APP_PATH)
    Notepad.open_new_tab()
    Notepad.tab_count_is_correct(2)
    Notepad.open_new_tab()
    Notepad.open_new_tab()
    Notepad.open_new_tab()
    Notepad.tab_count_is_correct(5)
