import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getBaseURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')