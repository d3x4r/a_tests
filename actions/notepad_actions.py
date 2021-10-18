class NotepadActions():
    def __init__(self, app):
        self.app = app

    def open(self, path):
        self.app.start(path)

    def open_new_tab(self):
        window = self.app.window(class_name='Notepad++')
        window.menu_select("File->New")

    def tab_count_is_correct(self, count):
        window = self.app.window(class_name='Notepad++')
        tab_count = window.Tab.tab_count()
        assert tab_count == count
