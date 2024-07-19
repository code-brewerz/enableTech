import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getCourseURL():
        return config.get('common info', 'courseURL')

    @staticmethod
    def getSauceURL():
        return config.get('common info', 'sauceURL')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def getFname():
        return config.get('common info', 'fname')

    @staticmethod
    def getLname():
        return config.get('common info', 'lname')

    @staticmethod
    def getZipcode():
        return config.get('common info', 'zipcode')


def initialize_creds():
    fname = ReadConfig.getFname()
    lname = ReadConfig.getLname()
    zipcode = ReadConfig.getZipcode()
    return fname, lname, zipcode
