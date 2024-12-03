from abc import ABC, abstractmethod
from pandas import Series
from entities.asset import Asset
from actions import Signal

class Strategy(ABC):
    def __init__(self, assets: Series[Asset]) -> None:
      self.assets = assets
      
    @abstractmethod
    def get_signal(self):
        pass
    
    @abstractmethod
    def calculate(self) -> Signal:
        pass