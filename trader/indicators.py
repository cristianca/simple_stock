from functools import reduce


def volume_weighted_price(trades):
    if not isinstance(trades, list):
        raise TypeError('the trades parameter should be a list')

    volume = 0
    price_quantity = 0

    for trade in trades:
        volume += trade.quantity
        price_quantity += trade.quantity * trade.price

    return price_quantity / volume


def geometric_mean(trades):
    if not isinstance(trades, list):
        raise TypeError('the trades parameter should be a list')

    prices = reduce(lambda x, y: x * y, [t.price for t in trades], 1)
    return prices ** (1 / len(trades))
