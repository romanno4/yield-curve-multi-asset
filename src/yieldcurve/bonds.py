import numpy as np


def cashflows(maturity, coupon_rate, freq=2, face=100):
    """Dates (en années) et montants des flux d'une obligation."""
    n = int(np.ceil(maturity * freq - 1e-9))         # nb de coupons restants
    times = maturity - np.arange(n)[::-1] / freq     # dates comptées depuis l'échéance
    amounts = np.full(n, face * coupon_rate / freq)                 # coupon par période : face * taux / freq
    amounts[-1] += face                       # au dernier flux, on rembourse le nominal
    return times, amounts


def bond_price(times, amounts, rate_fn):
    """Somme des flux actualisés ; rate_fn(t) donne le taux zéro à t."""
    rates = rate_fn(times)
    return np.sum(amounts * np.exp(-rates * times))                              # somme de amounts * e^(-rates * times)