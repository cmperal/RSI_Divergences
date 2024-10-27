from external_services.alpha_vantage import AlphaVantage
from api_config import Api_config
from strategies.rsi_divergences import RSIDivergences
from entities.asset import Asset
import pandas as pd

CONFIG_API_FILE = "api_config_paper_mode.json"

#Logic to calculate RSI Divergences (paper mode)
api_config = Api_config(CONFIG_API_FILE)
alphaVantage = AlphaVantage(api_config)
response = alphaVantage.get_monthly_time_series('AAPL')
assets = Asset.from_json_timeline(response)
rsi_divergences = RSIDivergences(assets)
print(response)