import requests

class Alpaca:    
    
    def __init__(self, api_config):
        self.data_base_url = api_config.apca_data_base_url        
        self.headers = {            
            "APCA-API-KEY-ID": api_config.apca_api_key,
            "APCA-API-SECRET-KEY": api_config.apca_secret_key,
            "accept": "application/json",
        }       
    
    def get_asset_by_symbol(self, symbol, params=None):
        # "https://data.alpaca.markets/v2/stocks/bars?symbols=AAPL&timeframe=1Month&limit=20&adjustment=raw&feed=sip&sort=asc"
        url = f"{self.data_base_url}/stocks/bars?symbols={symbol}&timeframe=1Week&limit=20&adjustment=raw&feed=sip&sort=asc"
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)        