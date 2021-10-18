import pytest
from pywinauto.application import Application


@pytest.fixture()
def app(request):
    app = Application(backend='uia')

    yield app

    app.kill()
