import numpy as np
from yieldcurve.bonds import bond_price


def shifted_price(times, amounts, rate_fn, h):
    """Prix si toute la courbe est décalée de h (choc parallèle)."""
    return bond_price(times, amounts, lambda t: rate_fn(t) + h)


def risk_measures(times, amounts, rate_fn, h=1e-4):
    p0 = shifted_price(times, amounts, rate_fn, 0)
    p_up = shifted_price(times, amounts, rate_fn, +h)
    p_down = shifted_price(times, amounts, rate_fn, -h)
    dv01 = (p_down - p_up) / 2
    duration = (p_down - p_up) / (2 * p0 * h)
    convexity = (p_up + p_down - 2 * p0) / (p0 * h**2)
    return {"price": p0, "dv01": dv01, "duration": duration, "convexity": convexity}