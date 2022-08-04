class ConfigValues:

    __instance = None

    @staticmethod
    def getInstance():
        if ConfigValues.__instance == None:
            ConfigValues()
        return ConfigValues.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ConfigValues.__instance != None:
            raise Exception("This calss is a singleton!")
        else:
            ConfigValues.__instance = self

s = ConfigValues()
print(s)

s = ConfigValues.getInstance()
print(s)

s = ConfigValues.getInstance()
print(s)
