import sys
sys.path.insert(0, "src")
from yieldcurve.data import load_treasury_curve
from yieldcurve.nelson_siegel import ns_rate, fit_ns
from yieldcurve.bonds import cashflows, bond_price

c = load_treasury_curve("2023-01-01", "2023-12-31")
mat = c.columns.to_numpy(dtype=float)
p = fit_ns(mat, c.loc["2023-07-03"].to_numpy())

curve = lambda t: ns_rate(t, *p)              # la courbe devient une fonction
times, amounts = cashflows(6.3, 0.04)
print("Dates :", times)
print("Taux NS à 6,3 ans :", round(curve(6.3) * 100, 2), "%")
print("Prix :", round(bond_price(times, amounts, curve), 2))