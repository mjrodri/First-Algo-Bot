# Starting by importing test data
# Must first install libraries

import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2000-01-01", end="2023-11-30", interval='15m')
dataF.iloc[-1:,:]
dataF.Open.iloc
