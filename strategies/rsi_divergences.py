
from strategies.strategy import Strategy


class RSIDivergences(Strategy):
    def __init__(self, price_history):
        self.price_history = price_history
        
    def get_signal(self):
        return 'buy'
    
    def calculate(self):
        #Check if latest close price is greater than previous (UP) or not (DOWN)
        
        
        return ""