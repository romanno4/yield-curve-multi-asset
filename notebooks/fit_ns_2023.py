import sys
sys.path.insert(0, "src")

import numpy as np
import matplotlib.pyplot as plt
from yieldcurve.data import load_treasury_curve
from yieldcurve.nelson_siegel import ns_rate, fit_ns

c = load_treasury_curve("2023-01-01", "2023-12-31")
mat = c.columns.to_numpy(dtype=float)
r = c.loc["2023-07-03"].to_numpy()

p = fit_ns(mat, r)
print("Paramètres :", p)
print("Écarts (pb) :", ((ns_rate(mat, *p) - r) * 10000).round(1))

t = np.linspace(0.05, 30, 300)
plt.plot(mat, r, "o", label="marché")
plt.plot(t, ns_rate(t, *p), label="Nelson-Siegel")
plt.xlabel("Maturité (années)"); plt.ylabel("Taux")
plt.title("Courbe US Treasury, 3 juillet 2023")
plt.legend(); plt.show()