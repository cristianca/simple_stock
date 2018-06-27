from datetime import datetime
from unittest import TestCase

from trader.trade import TradeDirection, Trade


class TestTradeDirection(TestCase):
    def test_class_has_needed_directions(self):
        """
        test the stock type enum for the two attributed needed
        """
        self.assertTrue(hasattr(TradeDirection, 'buy'))
        self.assertTrue(hasattr(TradeDirection, 'sell'))


class TestTrade(TestCase):
    def setUp(self):
        self.timestamp = datetime.now()
        self.trade = Trade(self.timestamp, 10, TradeDirection.sell, 23.6)

    def test_class_has_required_properties(self):
        self.assertTrue(hasattr(self.trade, 'timestamp'))
        self.assertTrue(hasattr(self.trade, 'quantity'))
        self.assertTrue(hasattr(self.trade, 'direction'))
        self.assertTrue(hasattr(self.trade, 'price'))

    def test_set_properties(self):
        self.assertEqual(self.trade.timestamp, self.timestamp)
        self.assertEqual(self.trade.quantity, 10)
        self.assertEqual(self.trade.direction, TradeDirection.sell)
        self.assertEqual(self.trade.price, 23.6)

    def test_setter_timestamp_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.timestamp = '2018-01-01 12:30:00'

    def test_setter_quantity_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.quantity = "10"

    def test_setter_direction_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.direction = 1

    def test_setter_price_raises_error(self):
        with self.assertRaises(TypeError):
            self.trade.price = "10"
