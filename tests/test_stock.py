from unittest import TestCase

from trader.stock import StockType, PreferredStock, CommonStock


class TestStockType(TestCase):
    def test_class_has_stock_attributes(self):
        """
        test the stock type enum for the two attributed needed
        """
        self.assertTrue(hasattr(StockType, 'common'))
        self.assertTrue(hasattr(StockType, 'preferred'))


class TestStock(TestCase):
    def setUp(self):
        self.common_stock = CommonStock('TEA', 3, 100)
        self.preferred_stock = PreferredStock('GIN', 8, 100, 2)

    def test_class_has_required_properties(self):
        self.assertTrue(hasattr(self.common_stock, 'symbol'))
        self.assertTrue(hasattr(self.common_stock, 'last_dividend'))
        self.assertTrue(hasattr(self.preferred_stock, 'fixed_dividend'))
        self.assertTrue(hasattr(self.common_stock, 'par_value'))

    def test_init_param_none_sets_zero(self):
        stock = PreferredStock(symbol='GIN', last_dividend=0, par_value=0)
        self.assertEqual(stock.fixed_dividend, 0)

    def test_dividend_yield_value(self):
        self.assertEqual(self.common_stock.dividend_yield(market_price=12.5), 0.24)
        self.assertEqual(self.preferred_stock.dividend_yield(market_price=40), 5)

    def test_dividend_yield_raises_error(self):
        with self.assertRaises(ValueError):
            self.common_stock.dividend_yield(None)
        with self.assertRaises(ValueError):
            self.common_stock.dividend_yield(0)

    def test_pe_ratio_value(self):
        self.assertAlmostEqual(self.common_stock.pe_ratio(market_price=12.5), 12.5 / 0.24)
        self.assertEqual(self.preferred_stock.pe_ratio(market_price=40), 40 / 5)

    def test_pe_ratio_raises_error(self):
        stock = CommonStock('TEA', 0, 100)
        with self.assertRaises(ValueError):
            stock.pe_ratio(12)
