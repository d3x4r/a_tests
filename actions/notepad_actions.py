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

    def write_text_to_tab(self, text):
        window = self.app.window(class_name='Notepad++')
        window.type_keys(text, with_spaces=True)
        assert window.child_window(class_name='Scintilla').texts()[0] == text
