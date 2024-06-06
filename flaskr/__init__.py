import os

from flask import Flask, render_template, request
from StockAPI import get_stock_market
from Stock import Stock
from StockStatistics import day_statistics

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev', 
        DATABASE = os.path.join(app.instance_path, 'flaske.sqlite'),
    )

    if test_config is None:
       #Load the instance config, if it exists, when not testing
       app.config.from_pyfile('config.py', silent = True)
    else:
        #load the test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')
    
    @app.route('/stock')
    def get_stock():
        stock_name = request.args.get('Stock')
        stock_data = get_stock_market(stock_name)
        stock_statistics = day_statistics(stock_data)
        return render_template(
            "Stock.html",
            title=Stock.get_name(stock_data),
            update_day=Stock.get_update_date(stock_data),
            invest=True if stock_statistics > 0 else False
        )
    
    return app
