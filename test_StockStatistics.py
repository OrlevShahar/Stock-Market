import unittest
from Stock import Stock
import StockStatistics
import json

class TestStockStatistics(unittest.TestCase):
    def setUp(self):
        file_path = 'tester.txt'
        with open(file_path, 'r') as file: 
            self.data = json.load(file)
        self.stock1 = Stock(self.data)
    
    # I know it's not needed, but it's for me to remember it exists
    def tearDown(self):
        pass

    def test_day_statistics(self):
        self.assertIsNotNone(StockStatistics.day_statistics(self.stock1))
        self.assertEqual(StockStatistics.day_statistics(self.stock1), 1)



if __name__ == '__main__':
    unittest.main()