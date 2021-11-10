import pytest
import importlib
from selenium import webdriver
from pywinauto.application import Application


browser_list = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    normalized_name = browser_name.lower()

    if normalized_name not in browser_list.keys():
        raise BaseException('wrong browser')

    browser = browser_list[normalized_name]()

    yield browser

    browser.quit()


@pytest.fixture()
def notepad(request):
    app = Application(backend='uia')

    yield app

    app.kill()


@pytest.fixture()
def java_app(request):
    RemoteSwingLibrary = importlib.import_module('RemoteSwingLibrary')
    java_app = RemoteSwingLibrary.RemoteSwingLibrary()

    yield java_app

    java_app.system_exit()
