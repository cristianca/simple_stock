from enum import Enum


class StockType(Enum):
    common = "COMMON"
    preferred = "PREFERRED"


class BaseStock(object):
    def __init__(self, symbol, last_dividend, par_value):
        self.symbol = symbol
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.trades = []

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if value is None:
            raise ValueError
        self._symbol = value

    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Last dividend should be int or float')
        self._last_dividend = value

    @property
    def par_value(self):
        return self._par_value

    @par_value.setter
    def par_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Last dividend should be int or float')
        self._par_value = value

    def dividend_yield(self, market_price):
        """
        calculate the dividend based on the price and type of stock
        :param market_price: the current market price of the stock
        :return: will return the dividend yield
        :raises NotImplementedError if unknown stock type
        :raises ValueError if market price is None or 0
        """
        raise NotImplementedError

    def pe_ratio(self, market_price):
        """
        calculate the P/E ratio
        :param market_price: the current market price of the stock
        :return: P/E ratio
        :raises ValueError if division by zero
        """
        dividend = self.dividend_yield(market_price)
        if dividend > 0.0:
            return market_price / dividend
        else:
            raise ValueError('Dividend field is zero')


class CommonStock(BaseStock):
    def dividend_yield(self, market_price):
        if market_price is None or market_price == 0:
            raise ValueError('Market price is zero')

        return self.last_dividend / market_price


class PreferredStock(BaseStock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend=None):
        super(PreferredStock, self).__init__(symbol, last_dividend, par_value)
        self.fixed_dividend = fixed_dividend

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, value):
        self._fixed_dividend = float(value or 0)

    def dividend_yield(self, market_price):
        if market_price is None or market_price == 0:
            raise ValueError('Market price is zero')

        return (self.fixed_dividend * self.par_value) / market_price
