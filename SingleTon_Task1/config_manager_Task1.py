from abc import ABC, abstractmethod


class ConfigManager(ABC):

    def __init__(self):
        # Configuration data should be stored here.
        self.properties = {}

    @abstractmethod
    def get_configuration(self, key, value_type=None):
        raise NotImplementedError("Implement in child class")

    @abstractmethod
    def set_configuration(self, key, value):
        # TODO: Implement in child class
        pass

    @abstractmethod
    def remove_configuration(self, key):
        # TODO: Implement in child class
        pass

    @abstractmethod
    def clear(self):
        # TODO: Implement in child class
        pass
