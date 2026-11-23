import numpy as np 
from scipy.optimize import least_squares

def ns_rate(t, b0, b1, b2, tau):
    t=np.asarray(t, dtype=float)
    x = t / tau
    expo = np.exp(-x)
    f1 = (1 - expo) / x
    f2 = f1 - expo
    return b0 + b1 * f1 + b2 * f2

    

def fit_ns(maturities, rates):
    def residuals(p):
        return ns_rate(maturities, *p) - rates
    x0 = [rates[-1], rates[0] - rates[-1], 0.0, 2.0]
    res = least_squares(residuals, x0, bounds=([-1, -1, -1, 0.05], [1, 1, 1, 30]))
    return res.x