import sys
sys.path.insert(0, "src")
from yieldcurve.data import load_treasury_curve
from yieldcurve.nelson_siegel import ns_rate, fit_ns
from yieldcurve.bonds import cashflows
from yieldcurve.risk import risk_measures, shifted_price

c = load_treasury_curve("2023-01-01", "2023-12-31")
mat = c.columns.to_numpy(dtype=float)
p = fit_ns(mat, c.loc["2023-07-03"].to_numpy())
curve = lambda t: ns_rate(t, *p)

for maturity, coupon in [(6.3, 0.04), (10, 0.0), (30, 0.04)]:
    times, amounts = cashflows(maturity, coupon)
    m = risk_measures(times, amounts, curve)
    print(f"{maturity:>4} ans, coupon {coupon:.0%} : " +
          ", ".join(f"{k} = {v:.4f}" for k, v in m.items()))

# Vérification : choc de +100 pb, vrai prix contre approximation
times, amounts = cashflows(6.3, 0.04)
m = risk_measures(times, amounts, curve)
dr = 0.01
exact = shifted_price(times, amounts, curve, dr) - m["price"]
approx = m["price"] * (-m["duration"] * dr + 0.5 * m["convexity"] * dr**2)
print(f"+100 pb : exact {exact:.2f}, approx D+C {approx:.2f}")