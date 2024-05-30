import requests
import os
import json
from Stock import Stock
import StockStatistics

def main():
    file_path = 'test.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file: 
            data = json.load(file)
        
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=UFIT9YCNQS2J1C5G'
        r = requests.get(url)
        data = r.json()
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    stock_market = Stock(data)
    #Stock.print_stock_array(stock_market)
    success_rate = StockStatistics.day_statistics(stock_market)
    print(f"the success rate is: {success_rate}")

    

    


if __name__ == '__main__': 
    main()