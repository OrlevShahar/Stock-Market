import unittest
from src.stock import Stock
import json

class TestStock(unittest.TestCase):

    def setUp(self):
        file_path = file_path = "src/tests/data/tester.txt"
        with open(file_path, 'r') as file: 
            self.data = json.load(file)
        self.stock1 = Stock(self.data)

    # I know it's not needed, but it's for me to remember it exists
    def tearDown(self):
        pass
        
    def test_get_name(self):
        self.assertIsNotNone(Stock.get_name(self.stock1))
        self.assertEqual(Stock.get_name(self.stock1), self.data['Meta Data']["2. Symbol"])

    def test_get_update_date(self):
        self.assertIsNotNone(Stock.get_update_date(self.stock1))
        self.assertEqual(Stock.get_update_date(self.stock1), self.data['Meta Data']["3. Last Refreshed"])
    
    
    def test_get_stock_array(self):
        stock_array = Stock.get_stock_array(self.stock1)
        self.assertIsNotNone(stock_array)

        #Check that the lengths are the same
        self.assertEqual(len(stock_array), len(self.data["Time Series (Daily)"]))

        #Check if all the entries are the same and in the correct order (in the array, the new dates are at the end of the array)
        json_dates = list(self.data["Time Series (Daily)"].keys())
        for i in range(len(stock_array)):
            json_date = json_dates[len(json_dates) - i - 1]
            json_entry = self.data["Time Series (Daily)"][json_date]

            self.assertEqual(stock_array[i]["date"], json_date)
            self.assertEqual(stock_array[i]["open"], float(json_entry["1. open"]))
            self.assertEqual(stock_array[i]["close"], float(json_entry["4. close"]))
    
    def test_get_change_date_dict(self):
        stock_dict = Stock.get_change_date_dict(self.stock1)
        self.assertIsNotNone(stock_dict)

        # Check if all the entries in the JSON are in the correct bucket in the hashmap
        for date, daily_data in self.data["Time Series (Daily)"].items():

            change = float(daily_data["4. close"])/float(daily_data["1. open"])
            change = round(change,3)

            self.assertIn(date, stock_dict[change])


    

if __name__ == '__main__':
    unittest.main()