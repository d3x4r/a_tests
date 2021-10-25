import pytest
from actions.mediator import Mediator
from actions.base_actions import BaseActions


@pytest.mark.parametrize("description_text", ['', '111111111111111', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaa bbbbbbbbbbbbb', '!@#$%^&*()_+'])
def test_description_input(app, description_text):
    APP_PATH = './src/TodoListApplication.java'

    JavaApp = BaseActions(Mediator(), app)
    JavaApp.open(APP_PATH)
    JavaApp.write_description_text(description_text)


@pytest.mark.parametrize("todo_items", [['first_todo'], ['first_todo', 'second_todo'], ['first_todo', 'second_todo', 'third_todo']])
def test_add_todo_item(app, todo_items):
    APP_PATH = './src/TodoListApplication.java'

    JavaApp = BaseActions(Mediator(), app)
    JavaApp.open(APP_PATH)

    for todo_text in todo_items:
        JavaApp.write_description_text(todo_text)
        JavaApp.add_todo_item()

    JavaApp.todo_items_is_correct(len(todo_items))
