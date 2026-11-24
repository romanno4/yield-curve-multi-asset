import sys
sys.path.insert(0, "src")
import numpy as np
from yieldcurve.bonds import cashflows, bond_price

flat = lambda t: np.full_like(t, 0.04)        # courbe plate à 4 %
print(bond_price(*cashflows(10, 0.0), flat))  # zéro-coupon 10 ans
print(bond_price(*cashflows(10, 0.04), flat)) # coupon 4 % 10 ans