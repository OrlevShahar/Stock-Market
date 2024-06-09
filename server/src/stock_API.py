from dotenv import load_dotenv
from stock import Stock
import json
import requests
import os
import logging


load_dotenv()

def get_stock_market(stock_name):
        
    file_path = f"server/src/data/{stock_name}.txt"
    logging.info(f"the file path is: {file_path}")
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file: 
            data = json.load(file)
        
    else:
        # APIKEY is from www.alphavantage.co
        # will add cache in the near future
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={os.getenv("API_KEY")}'
        print(url)
        r = requests.get(url)
        data = r.json()
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    stock_market = Stock(data)

    return stock_market
    


if __name__ == "__main__":
    print('\n --- get the stock market data ---\n')

    stock_name = input("\n please enter a stock name: ")

    stock_market = get_stock_market(stock_name)

    Stock.print_stock_array(stock_market)