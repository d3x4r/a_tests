from abc import ABC
from .browser_actions import BrowserActions
from .notepad_actions import NotepadActions
from selenium.webdriver import Firefox, Chrome
from enum import Enum
from .base_actions import EventType


class AppType(Enum):
    NOTEPAD = 1
    WEB = 2


class IMediator(ABC):
    def notify(self, sender, event_type, *args): pass


class Mediator(IMediator):
    def check_sender_type(self, app):

        if isinstance(app, Firefox) or isinstance(app, Chrome):
            return AppType.WEB
        else:
            # ToDo Добавить проверку по типу
            return AppType.NOTEPAD

    def notify(self, sender, event_type, *args):
        sender_type = self.check_sender_type(sender.app)

        if event_type == EventType.INIT:

            if sender_type == AppType.WEB:
                BrowserActions.__init__(sender, sender.app)

            if sender_type == AppType.NOTEPAD:
                NotepadActions.__init__(sender, sender.app)

        elif event_type == EventType.OPEN:

            if sender_type == AppType.WEB:
                BrowserActions.open(sender, *args)

            if sender_type == AppType.NOTEPAD:
                NotepadActions.open(sender, *args)
