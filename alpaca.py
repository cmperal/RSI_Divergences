import requests

class Alpaca:    
    
    def __init__(self, api_config):
        self.base_url = api_config.base_url
        self.headers = {            
            "APCA-API-KEY-ID": api_config.api_key,
            "APCA-API-SECRET-KEY": api_config.secret_key,
            "accept": "application/json",
        }       
    
    def get_asset(self, params=None):
        url = f"{self.base_url}/assets/BTC%2FUSDT"
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)        