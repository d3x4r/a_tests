from abc import ABC, abstractmethod
from enum import Enum
from .browser_actions import BrowserActions
from .notepad_actions import NotepadActions
from .java_actions import JavaActions


class EventType(Enum):
    INIT = 1
    OPEN = 2


class IBaseActions(ABC):
    @abstractmethod
    def __init__(self, mediator, app): pass

    @abstractmethod
    def open(self, value): pass


class BaseActions(IBaseActions, BrowserActions, NotepadActions, JavaActions):
    def __init__(self, mediator, app):
        self.mediator = mediator
        self.app = app
        self.mediator.notify(self, EventType.INIT)

    def open(self, value):
        self.mediator.notify(self, EventType.OPEN, value)
