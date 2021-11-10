from actions.base_actions import BaseActions
from actions.mediator import Mediator


def test_copy_text_from_browser_and_write_to_desktop_apps(browser, notepad, java_app):
    mediator = Mediator()
    LINK = 'http://ya.ru'
    SEARCH_TEXT = 'text'
    NOTEPAD_PATH = r'C:\Program Files\Notepad++\notepad++.exe'
    JAVA_APP_PATH = './src/TodoListApplication.java'

    Firefox = BaseActions(mediator, browser)
    Firefox.open(LINK)
    Firefox.write_search_text(SEARCH_TEXT)
    Firefox.submit_search_form()
    title = Firefox.get_first_result_item_title()

    Notepad = BaseActions(mediator, notepad)
    Notepad.open(NOTEPAD_PATH)
    Notepad.write_text_to_tab(title)

    JavaApp = BaseActions(mediator, java_app)
    JavaApp.open(JAVA_APP_PATH)
    JavaApp.write_description_text(title)
