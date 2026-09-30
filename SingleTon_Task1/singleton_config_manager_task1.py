from config_manager_Task1 import ConfigManager


class FileBasedConfigurationManager(ConfigManager):

    # TODO:
    # Store the Singleton instance here.
    _instance = None
    _intialized=False

    def __new__(cls):  #create a new instance of the class
        # TODO:
        if(cls._instance is None):
            cls._instance = super().__new__(cls)
        return cls._instance
        # Control object creation so that only one
        # FileBasedConfigurationManager object exists.
        pass

    def __init__(self): #
        # TODO:
        print("init called")
        if not getattr(self, "_intialized", False):
            super().__init__()
            self._intialized=True
        # Initialize the parent class.
        # Be careful: __init__ can run more than once
        # when using a Singleton with __new__.
        pass

    @classmethod
    def get_instance(cls):
        # TODO:
        return cls()
        # Return the Singleton instance.
        pass

    @classmethod
    def reset_instance(cls):
        # TODO:
        # Reset the Singleton instance.
        pass

    def get_configuration(self, key, value_type=None):
        value = self.properties.get(key)
        if value is None or value_type is None:
            return value
        return value_type(value)

    def set_configuration(self, key, value):
        # TODO:
        self.properties[key]=value
        # Store the configuration.
        pass

    def remove_configuration(self, key):
        # TODO:
        # Remove the configuration if it exists.
        pass

    def clear(self):
        # TODO:
        # Remove all configurations.
        pass
