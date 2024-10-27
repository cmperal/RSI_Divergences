import pandas as pd
import datetime as dt

class Asset:
    def __init__(self, date: dt, open: float, high: float, low: float, close: float, adjusted_closed: float, volume: int, divided_amount: float):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adjusted_closed = adjusted_closed
        self.volume = volume
        self.divided_amount = divided_amount
        
     # Class method to map the JSON timeline to a list of Asset objects
    @classmethod
    def from_json_timeline(cls, timeline):
       # Convert the dictionary to a DataFrame and transpose it so that dates are rows
        df = pd.DataFrame(timeline).T

        # Reset the index to turn dates into a column
        df.reset_index(inplace=True)

        # Rename the columns for clarity
        df.columns = ['date', 'open', 'high', 'low', 'close', 'adjusted_closed', 'volume', 'divided_amount']
                 
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        # Apply the function to each row of the DataFrame and convert to a list of StockData objects
        asset_list = df.apply(cls.map_to_asset_data, axis=1)        
               
        return asset_list.sort_index(ascending=False)
        
    @classmethod   
    def map_to_asset_data(cls, row):
        return Asset(            
            date=row.name,
            open=row['open'],
            high=row['high'],
            low=row['low'],
            close=row['close'],
            adjusted_closed=row['adjusted_closed'],
            volume=row['volume'],
            divided_amount=row['divided_amount']
        )