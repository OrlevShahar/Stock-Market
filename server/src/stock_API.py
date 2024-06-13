from dotenv import load_dotenv
from stock import Stock
import json
import requests
import os
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

def get_stock_market(stock_name):
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    file_path = os.path.join(base_dir, f"{stock_name}.txt")
    logging.info(f"the file path is: {file_path}")
    
    if os.path.exists(file_path):
        logging.info("Loading data from file.")
        with open(file_path, 'r') as file: 
            data = json.load(file)
        
    else:
        # APIKEY is from www.alphavantage.co
        # will add cache in the near future
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={os.getenv("API_KEY")}'
        logging.info(f"the url is: {url}")
        r = requests.get(url)
        data = r.json()
        #chack if error in api (it will start in 'Error Message')
        if 'Error Message' in data:
            logging.error("Error in API call.")
            return 'Error Message'
        
        logging.info("Saving data to file.")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    stock_market = Stock(data)

    return stock_market
    


if __name__ == "__main__":
    print('\n --- get the stock market data ---\n')

    stock_name = input("\n please enter a stock name: ")

    stock_market = get_stock_market(stock_name)

    Stock.print_stock_array(stock_market)