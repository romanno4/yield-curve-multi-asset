import pandas as pd

TENORS = {"DGS1MO": 1/12, "DGS3MO": 0.25, "DGS6MO": 0.5, "DGS1": 1, "DGS2": 2,
          "DGS3": 3, "DGS5": 5, "DGS7": 7, "DGS10": 10, "DGS20": 20, "DGS30": 30}
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"

def load_treasury_curve(start: str, end: str | None = None) -> pd.DataFrame:
    """Rendements US Treasury en décimal, colonnes = maturités en années."""
    series = [pd.read_csv(URL.format(c), index_col=0, parse_dates=True,
                          na_values=".").squeeze("columns").rename(t)
              for c, t in TENORS.items()]
    df = pd.concat(series, axis=1).loc[start:end] / 100
    return df.dropna()