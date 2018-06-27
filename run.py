import csv
import datetime
from random import randint, choice, random

import itertools

from trader.indicators import volume_weighted_price, geometric_mean
from trader.stock import StockType, CommonStock, PreferredStock
from trader.trade import Trade, TradeDirection


def read_stock_data():
    """
    read stock data from a comma separated file
    The csv file should have the following format:
        - the first line should be the header: symbol,type,last dividend,fixed dividend,par value
        - the other lines should contain all the info described in the header
    :return: a list of Stock objects
    """
    stocks = []
    with open('stocks.csv', 'r') as stock_file:
        reader = csv.reader(stock_file)
        next(reader, None)  # skip the header
        for row in reader:
            symbol = row[0]
            last_dividend = float(row[2])
            par_value = float(row[4])
            if row[1].upper() == StockType.common.value:
                stocks.append(CommonStock(symbol=symbol, last_dividend=last_dividend, par_value=par_value))
            elif row[1].upper() == StockType.preferred.value:
                fixed_dividend = float(row[3])
                stocks.append(PreferredStock(symbol=row[0], last_dividend=last_dividend, fixed_dividend=par_value,
                                             par_value=fixed_dividend))
            else:
                print('Error: Stock type unknown')
    return stocks


def generate_trade_data(stock):
    """
    generate between 15 or 50 min of trade data for stocks. New trade object will be created for every minute.
    :param stock: the stock object that will have the trades list generated
    """
    stock.trades = []
    number_of_trades = randint(15, 50)

    for index in range(number_of_trades):
        timestamp = datetime.datetime.now() - datetime.timedelta(minutes=index)
        direction = choice([TradeDirection.buy, TradeDirection.sell])
        price = random() * 100
        stock.trades.append(Trade(timestamp, quantity=randint(1, 30), direction=direction, price=price))


def filter_trades(trades):
    """
    filter the trades list and get only the trades from the last 15 min
    :param trades: trade list
    :return: only trades within the last 15 min.
    """
    trade_start_date = datetime.datetime.now() - datetime.timedelta(minutes=15)
    return list(filter(lambda trade: trade.timestamp > trade_start_date, trades))


if __name__ == "__main__":
    stocks = read_stock_data()
    print("Calculate stock dividend yield and P/E Ratio")
    print("Stock | Dividend yield | P/E Ratio")
    for stock in stocks:
        price = randint(1, 300)
        try:
            print(f'{stock.symbol: >5} | {stock.dividend_yield(price):>14.4f} | {stock.pe_ratio(price):>9.4f}')
        except ValueError as e:
            print(str(e).center(34))

    for stock in stocks:
        generate_trade_data(stock)

    print("Calculate Volume Weighted Stock Price based on trades in past 15 minutes")
    print("Symbol | Volume Weighted Stock Price")
    for stock in stocks:
        # make sure we only use 15 min of data for computing the volume weighted price
        last_trades = filter_trades(stock.trades)
        print(f"{stock.symbol: >6} | {volume_weighted_price(last_trades):.4f}")

    all_trades = list(itertools.chain.from_iterable([stock.trades for stock in stocks]))
    mean = geometric_mean(all_trades)
    print(f"Calculate the GBCE All Share Index : {mean}")
