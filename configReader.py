from configparser import ConfigParser
import ast

class configReader:

    def __init__(self, configFile):

        self.config = ConfigParser() #Initialize config parser
        self.config.read(configFile) #Read specified config file
    
    def getAuthConfig(self, valueKey):
        value = self.config.get('Authentication', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value

    def getShutdownConfig(self, valueKey):
        value = self.config.get('Shutdown', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value
    
    def getPowerOnConfig(self, valueKey):
        value = self.config.get('Power On', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value

    def getKeypadConfig(self, valueKey):
        value = self.config.get('Keypad', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value

    def getLCDdriverConfig(self, valueKey):
        value = self.config.get('LCD Driver', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value

    def getLogConfig(self, valueKey):
        value = self.config.get('Log', valueKey) #Get value from config file
        value = ast.literal_eval(value) #Parse value into correct format
        return value #Return value