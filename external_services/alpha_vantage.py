import requests
import json

class AlphaVantage:    
    
    def __init__(self, api_config):
        self.data_base_url = api_config.alpha_vantage_base_url     
        self.alpha_vantage_key_api = api_config.alpha_vantage_key_api  
        
    
    def get_monthly_time_series(self, symbol, params=None):      
        url = f"{self.data_base_url}/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={self.alpha_vantage_key_api}"
        #response = requests.get(url, params=params)
        #TO DO: To map to entity
        # Save JSON response to a file
        # with open('response.json', 'w') as json_file:
        #     # Write the JSON data to the file (ensure it's formatted)
        #     json.dump( response.json()['Monthly Adjusted Time Series'], json_file, indent=4)
        with open('response.json', 'r') as json_file:
            return json.load(json_file)  # Load the JSON data
        #return response.json()['Monthly Adjusted Time Series']       