import pytest
from pywinauto.application import Application


@pytest.fixture()
def app(request):
    app = Application(backend='win32')

    yield app

    app.kill()
