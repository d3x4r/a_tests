class JavaActions():
    PORT = 8270
    TIMEOUT = 30

    def __init__(self, app):
        self.app = app

    def open(self, app_path):
        command = f'java {app_path}'
        self.app.start_application('alias', command=command, stdout='./stdout.txt',
                                   stderr='./stderr.txt', remote_port=JavaActions.PORT, timeout=JavaActions.TIMEOUT)

    def write_description_text(self, text):
        IDENTIFIER = 'description'
        self.app.run_keyword('selectMainWindow', args=[])
        self.app.run_keyword('insertIntoTextField', args=[IDENTIFIER, text])
        result_text = self.app.run_keyword(
            'getTextFieldValue', args=[IDENTIFIER])
        assert result_text == text

    def add_todo_item(self):
        IDENTIFIER = 'Add Todo item'
        self.app.run_keyword('pushButton', args=[IDENTIFIER])

    def todo_items_is_correct(self, expected_count):
        IDENTIFIER = 'todolist'
        count = self.app.run_keyword('getListItemCount', args=[IDENTIFIER])
        assert count == expected_count
