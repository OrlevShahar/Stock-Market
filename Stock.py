import json


class Stock:
    """The class creates and manages the objects of a stock. 

    It has the following variables:
        self.name - the name of the company or the stock
        self.update - the last update date
        self.stock_array - an array of dates and the stock change for each date 
        self.change_date_dict - a mapping of the stock by its daily change
    """
    def __init__(self, stock_json):
        self.name = stock_json['Meta Data']["2. Symbol"]
        self.update = stock_json['Meta Data']["3. Last Refreshed"]
        self.stock_array = []
        self.change_date_dict = {}

        for date, daily_data in stock_json["Time Series (Daily)"].items():
            open_price = float(daily_data["1. open"])
            close_price = float(daily_data["4. close"])
            change = close_price/open_price
            change = round(change,3)

            stock_entry = {
                "date": date,
                "open": open_price, 
                "close": close_price,
                "change": change
            }

            self.stock_array.insert(0, stock_entry) #insert so the new date will be at the end 

            if change in self.change_date_dict:
                self.change_date_dict[change].append(date)
            else:
                self.change_date_dict[change] = [date]
   
 
    def get_name(self):
        return self.name

    def get_update_date(self):
        return self.update
    
    def get_stock_array(self):
        return self.stock_array
    
    def get_change_date_dict(self):
        return self.change_date_dict

    def get_update_information(self):
        return {
                    "open": self.stock_array[len(self.stock_array)-1]['open'], 
                    "close": self.stock_array[len(self.stock_array)-1]['close'], 
                    "change": self.stock_array[len(self.stock_array)-1]['change']
                } 
    
    def print_stock_array(self):
        for entry in self.stock_array:
            print (entry)
   