from ConfigManager import ConfigManager


class FileBasedConfigurationManager(ConfigManager):

    # TODO:
    # Store the Singleton instance here.
    _instance = None
    #memory alloction for a object -> object creation
    def __new__(cls):
        # TODO:
        if(cls._instance is None):
            cls._instance = super().__new__(cls)
        
        return cls._instance



    #init will initialize the attributes 
    def __init__(self):
        # TODO:
        if(hasattr(self,"_initialized")):
            return
        super().__init__()
        self._initialized = True

    @classmethod
    def get_instance(cls):
        # TODO:
        # Return the Singleton instance.
        pass

    @classmethod
    def reset_instance(cls):
        # TODO:
        # Reset the Singleton instance.
        pass

    def get_configuration(self, key, value_type=None):
        # TODO:
        # 1. Get the value using key.
        # 2. If it does not exist, return None.
        # 3. If value_type is None, return the value.
        # 4. Otherwise convert it to the requested type.
        val = self.properties.get(key)
        if(value_type == None):
            return val
        else:
            val = value_type(val)
            return val
        
    def set_configuration(self, key, value):
        # TODO:
        self.properties[key] = value

    def remove_configuration(self, key):
        # TODO:
        # Remove the configuration if it exists.
        pass

    def clear(self):
        # TODO:
        # Remove all configurations.
        pass