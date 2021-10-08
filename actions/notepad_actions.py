from selenium.webdriver.common.by import By
from .abstract_base_actions import AbstractBaseActions


class NotepadActions(AbstractBaseActions):
    def __init__(self, app):
        self.app = app

    def open(self, path):
        self.app.start(path)

    def connect(*args):
        return NotepadActions(*args)

    def open_new_tab(self):
        window = self.app["новый 1 - Notepad++ [Administrator]"]
        window.menu_select("Файл->Новый")

    def tab_count_is_correct(self, count):
        window = self.app["новый 1 - Notepad++ [Administrator]"]
        tab_count = window.child_window(
            title="Tab", class_name="SysTabControl32").tab_count()

        assert tab_count == count