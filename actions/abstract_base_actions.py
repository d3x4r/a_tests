from abc import ABC, abstractmethod

class AbstractBaseActions(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def connect(self):
        pass
