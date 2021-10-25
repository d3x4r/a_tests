import pytest
import importlib
import sys
import sys
import os

lib_dir = os.path.dirname('./')
sys.path.append(os.path.join(lib_dir, 'remoteswinglibrary-2.3.0.jar'))


@pytest.fixture()
def app(request):
    print(lib_dir)
    RemoteSwingLibrary = importlib.import_module('RemoteSwingLibrary')
    java_app = RemoteSwingLibrary.RemoteSwingLibrary()

    yield java_app

    java_app.system_exit()
