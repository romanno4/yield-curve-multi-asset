import numpy as np


def cashflows(maturity, coupon_rate, freq=2, face=100):
    """Dates (en années) et montants des flux d'une obligation."""
    n = int(round(maturity * freq))           # nombre de paiements
    times = np.arange(1, n + 1) / freq        # 0.5, 1.0, 1.5, ...
    amounts = np.full(n, face * coupon_rate / freq)                 # coupon par période : face * taux / freq
    amounts[-1] += face                       # au dernier flux, on rembourse le nominal
    return times, amounts


def bond_price(times, amounts, rate_fn):
    """Somme des flux actualisés ; rate_fn(t) donne le taux zéro à t."""
    rates = rate_fn(times)
    return np.sum(amounts * np.exp(-rates * times))                              # somme de amounts * e^(-rates * times)