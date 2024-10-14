import json

class Api_config:    
    def __init__(self, config_file):    
        self.config_file = config_file            
        self.config = self.__load_config()     
        self.base_url = self.config['BASE_URL']
        self.api_key = self.config['APCA-API-KEY-ID']
        self.secret_key = self.config['APCA-API-SECRET-KEY']
                  
    def __load_config(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        return config