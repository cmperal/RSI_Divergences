from alpaca import Alpaca
from api_config import Api_config

CONFIG_API_FILE = "api_config_paper_mode.json"

#Logic to calculate RSI Divergences (paper mode)
api_config = Api_config(CONFIG_API_FILE)
myAlpaca = Alpaca(api_config)
response = myAlpaca.get_asset()
print(response)