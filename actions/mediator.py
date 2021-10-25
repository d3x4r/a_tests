from abc import ABC

from actions.java_actions import JavaActions
from .browser_actions import BrowserActions
from .notepad_actions import NotepadActions
from selenium.webdriver import Firefox, Chrome
from enum import Enum
from .base_actions import EventType
import importlib


class AppType(Enum):
    NOTEPAD = 1
    WEB = 2
    JAVA = 3


class IMediator(ABC):
    def notify(self, sender, event_type, *args): pass


class Mediator(IMediator):
    def check_sender_type(self, app):
        RemoteSwingLibrary = importlib.import_module('RemoteSwingLibrary')
        if isinstance(app, Firefox) or isinstance(app, Chrome):
            return AppType.WEB
        elif(isinstance(app, RemoteSwingLibrary.RemoteSwingLibrary().__class__)):
            return AppType.JAVA
        else:
            # ToDo Добавить проверку по типу
            return AppType.NOTEPAD

    def notify(self, sender, event_type, *args):
        sender_type = self.check_sender_type(sender.app)

        if event_type == EventType.INIT:

            if sender_type == AppType.WEB:
                BrowserActions.__init__(sender, sender.app)

            elif sender_type == AppType.NOTEPAD:
                NotepadActions.__init__(sender, sender.app)

            elif sender_type == AppType.JAVA:
                JavaActions.__init__(sender, sender.app)

        elif event_type == EventType.OPEN:

            if sender_type == AppType.WEB:
                BrowserActions.open(sender, *args)

            elif sender_type == AppType.NOTEPAD:
                NotepadActions.open(sender, *args)

            elif sender_type == AppType.JAVA:
                JavaActions.open(sender, *args)
