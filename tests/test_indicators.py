from datetime import datetime
from unittest import TestCase

from trader.indicators import volume_weighted_price, geometric_mean
from trader.trade import Trade, TradeDirection


class TestIndicators(TestCase):
    def setUp(self):
        self.simple_trades = []
        self.double_trades = []
        self.complex_trades = []

        for index in range(10):
            self.simple_trades.append(Trade(datetime.now(), 1, TradeDirection.buy, 1))

        for index in range(10):
            self.double_trades.append(Trade(datetime.now(), 1, TradeDirection.buy, 2))

        for index in range(10):
            self.complex_trades.append(Trade(datetime.now(), (index + 1), TradeDirection.buy, (index + 1) * 2))

    def test_volume_weighted(self):
        self.assertEqual(volume_weighted_price(self.simple_trades), 1.0)
        self.assertEqual(volume_weighted_price(self.double_trades), 2.0)
        self.assertEqual(volume_weighted_price(self.complex_trades), 14.0)

    def test_geometric_mean(self):
        self.assertAlmostEqual(geometric_mean(self.simple_trades), 1.0)
        self.assertAlmostEqual(geometric_mean(self.double_trades), 2.0)
        self.assertAlmostEqual(geometric_mean(self.complex_trades), 9.05745737623353)