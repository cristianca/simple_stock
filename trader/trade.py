from datetime import datetime
from enum import Enum


class TradeDirection(Enum):
    buy = 1
    sell = 2


class Trade(object):
    def __init__(self, timestamp, quantity, direction, price):
        self.timestamp = timestamp
        self.quantity = quantity
        self.direction = direction
        self.price = price

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not isinstance(value, datetime):
            raise TypeError('The value should be a datetime object')
        self._timestamp = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Quantity should be numeric")
        self._quantity = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if not isinstance(value, TradeDirection):
            raise TypeError("Direction property should be of type TradeDirection")
        self._direction = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price should be a number')
        if value <= 0.0:
            raise ValueError('Price should be grater than 0')
        self._price = value
