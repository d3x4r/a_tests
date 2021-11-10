from actions.base_actions import BaseActions
from actions.mediator import Mediator


def test_count_tabs(app):
    APP_PATH = r'C:\Program Files\Notepad++\notepad++.exe'
    Notepad = BaseActions(Mediator(), app)
    Notepad.open(APP_PATH)
    Notepad.open_new_tab()
    Notepad.tab_count_is_correct(2)
