import json

class Api_config:    
    def __init__(self, config_file):    
        self.config_file = config_file            
        self.config = self.__load_config()     
        self.apca_broker_base_url = self.config['APCA_BROKER_BASE_URL']
        self.apca_data_base_url = self.config['APCA_DATA_BASE_URL']
        self.apca_api_key = self.config['APCA-API-KEY-ID']
        self.apca_secret_key = self.config['APCA-API-SECRET-KEY']
        self.alpha_vantage_base_url = self.config['ALPHA_VANTAGE_BASE_URL']
        self.alpha_vantage_key_api = self.config['ALPHA_VANTAGE_KEY_API']
                  
    def __load_config(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        return config