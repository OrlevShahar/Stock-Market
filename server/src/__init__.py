import os
from flask import Flask, render_template, request
from stock_API import get_stock_market  # Adjusted import based on the provided context
from stock import Stock  # Adjusted import based on the provided context
from stock_statistics import stock_score  # Import day_statistics

def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=os.path.join(os.path.dirname(__file__), '../../client/src/templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '../../client/src/static')
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config
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
        stock_name = request.args.get('stock')
        stock_data = get_stock_market(stock_name)
        stock_statistics = stock_score(stock_data)
        return render_template(
            "stock.html",
            title=Stock.get_name(stock_data),
            update_day=Stock.get_update_date(stock_data),
            invest=(stock_statistics > 0)
        )

    return app
