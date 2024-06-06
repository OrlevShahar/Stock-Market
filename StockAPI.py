from dotenv import load_dotenv
from Stock import Stock
import json
import requests
import os

load_dotenv()

def get_stock_market(stock_name = "TSCO.LON"):
    file_path = f"{stock_name}.txt"
    print(file_path)
    
    if os.path.exists(file_path):
        print("im hear2")
        with open(file_path, 'r') as file: 
            data = json.load(file)
        
    else:
        #the key is 5JDKHENL5MU9YQA0
        print("im hear")
        
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={os.getenv("API_KEY")}'
        print(url)
        r = requests.get(url)
        data = r.json()
        print(data)
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    stock_market = Stock(data)

    return stock_market
    


if __name__ == "__main__":
    print('\n --- get the stock market data ---\n')

    stock_name = input("\n please enter a stock name: ")

    stock_market = get_stock_market(stock_name)

    Stock.print_stock_array(stock_market)