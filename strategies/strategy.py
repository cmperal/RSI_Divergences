from abc import ABC, abstractmethod
from pandas import Series
from entities.asset import Asset

class Strategy(ABC):
    @abstractmethod
    def get_signal(self):
        pass
    
    @abstractmethod
    def calculate(self, assets: Series[Asset]) -> 
        pass