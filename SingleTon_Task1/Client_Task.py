from singleton_config_manager_task1 import FileBasedConfigurationManager


def main():

    # TODO 1:
    # Get the first Configuration Manager instance.
    config1 = FileBasedConfigurationManager.get_instance()
    config2 = FileBasedConfigurationManager.get_instance()

    # TODO 2:
    # Store configuration values.
    #
    config1.set_configuration("app.name", "MyApplication")
    config1.set_configuration("max.connections", 100)
    config1.set_configuration("timeout", 30.5)

    # TODO 3:
    # Read the configuration values.
    #
    print(config1.get_configuration("app.name"))
    print(config1.get_configuration("max.connections",float))
    print(config1.get_configuration("timeout"))

    config2.set_configuration("app.name","bhaiGadi_application")
    config2.set_configuration("max.connections",101)
    print(config1.get_configuration("app.name"))
    print(config1.get_configuration("max.connections"))

    # TODO 4:
    # Get the Singleton instance again.
    config2 = None

    # TODO 5:
    # Verify that config1 and config2 are the same object.
    #
    # print("Same instance:", ...)

    # TODO 6:
    # Remove the timeout configuration.
    #
    # config1.remove_configuration("timeout")
    # print("Timeout after removal:", ...)

    # TODO 7:
    # Clear all configurations.
    #
    # config1.clear()
    # print("App Name after clear:", ...)

    # TODO 8:
    # Reset the Singleton.
    #
    # FileBasedConfigurationManager.reset_instance()

    # TODO 9:
    # Get the Configuration Manager again.
    config3 = None

    # TODO 10:
    # Verify that config1 and config3 are different objects.
    #
    # print("New instance after reset:", ...)


if __name__ == "__main__":
    main()