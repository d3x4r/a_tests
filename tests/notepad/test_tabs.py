from actions.notepad_actions import NotepadActions


def test_search_input(app):
    APP_PATH = r'C:\Program Files\Notepad++\notepad++.exe'
    app = NotepadActions.connect(app)
    app.open(APP_PATH)
    app.open_new_tab()
    app.tab_count_is_correct(2)
    app.open_new_tab()
    app.open_new_tab()
    app.open_new_tab()
    app.tab_count_is_correct(5)