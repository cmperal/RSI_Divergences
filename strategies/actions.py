from enum import Enum

class Signal(Enum):
    BUY = 1
    SELL = 2
    SHORT = 3
    HOLD = 4
    COVER = 5
    STOP_LOSS = 6
    TAKE_PROFIT = 7