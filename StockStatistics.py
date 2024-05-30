from Stock import Stock
"""I really have a dilemma whether to turn this into a class. I think at this stage I'll leave it as is, 
but after I finish with the Flask topic and the software testing, I might revisit this.
Meanwhile, I am running the day_statistics function to add some substance to the project.
"""


"""Meanwhile, day_statistics is in its very early stages. 
It currently returns the number of stock market gains versus losses on dates with the same change as today.
"""
def day_statistics(stock):
    date_array = Stock.get_stock_array(stock)
    success = 0
    update_information = stock.get_update_information()
    for date in stock.change_date_dict[update_information["change"]]:
        index = date_binary_search(date, date_array)
        if (index != -1 and index + 1 < len(date_array)):
            next_day = date_array[index+1]
            if (next_day['change'] > 1):
                success = success + 1
            else:
                success = success - 1
    return success




def date_binary_search(date, stock_array):
    low = 0
    high = len(stock_array)-1
    while low <= high:
        mid = low + (high - low) // 2
        if stock_array[mid]['date'] == date:
            return mid
        
        if stock_array[mid]['date'] < date:
            low = mid +1
        else:
            high = mid -1
    return -1