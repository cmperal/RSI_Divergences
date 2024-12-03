from entities.asset import Asset
from pandas import Series
from strategies.strategy import Strategy


class RSIDivergences(Strategy):
    def __init__(self, assets: Series[Asset]):
        super().__init__(assets=assets)
        
    def get_signal(self):
        return 'buy'
    
    def calculate(self):
        #Check if previous close price is the minimum price within the latest 14 values
        #Check diff between shift() and roll()
        if (self.assets.min(14).adjusted_closed
        
        return ""