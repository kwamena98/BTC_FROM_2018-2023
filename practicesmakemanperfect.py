import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("12 Well-known Crypto(currency)  2018-2023.csv",index_col=False)

BTC=df[df.Type=="Bitcoin USD"]
ETH=df[df.Type=="Ethereum USD"]


btc_highs=BTC.High.values
eth_highs=ETH.High.values

BTC.loc[:, ('Date')] = pd.to_datetime(BTC['Date'])
years=BTC.Date.dt.year.values


btc_dates=BTC.Date


plt.plot(btc_dates,btc_highs,color='orange',label="BTC")


plt.ylabel("BTC")
plt.xlabel("DATE")

plt.legend()
plt.savefig('btc.png')

