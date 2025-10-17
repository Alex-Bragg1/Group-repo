# my_module/Plot.py
# Zavier and Freddie Branch - Updated for Final Submission
# Date Modified: 18 - 10 - 2025
# Description: Comparison of Nvidia and AMD using plots and better visuals

import matplotlib.pyplot as plt
import yfinance as yf
import os

# Create a folder to save plots
os.makedirs("plots", exist_ok=True)

# Downloading the dataset - NVDA = Nvidia, AMD = Advanced Micro Devices
data1 = yf.download("NVDA", start="2025-01-01", end="2025-09-15")
data2 = yf.download("AMD", start="2025-01-01", end="2025-09-15")

plt.style.use("seaborn-v0_8-darkgrid")

# === FIGURE 1: Closing Prices ===
plt.figure(figsize=(8, 5))
plt.plot(data1.index, data1['Close'], label='NVDA Close Price', color='royalblue', linewidth=2)
plt.plot(data2.index, data2['Close'], label='AMD Close Price', color='darkorange', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Comparing AMD and NVDA Closing Prices (YTD)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("plots/closing_prices.png", dpi=300)
plt.show()

# === FIGURE 2: Trade Volumes ===
plt.figure(figsize=(8, 5))
plt.plot(data1.index, data1['Volume'], label='NVDA Volume', color='royalblue', linewidth=2)
plt.plot(data2.index, data2['Volume'], label='AMD Volume', color='darkorange', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Trade Volumes of NVDA and AMD (YTD)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("plots/trade_volumes.png", dpi=300)
plt.show()

# === FIGURE 3: Intra-Day Volatility ===
data1['Volatility_NVDA'] = (data1['High'] - data1['Low']) / data1['Open']
data2['Volatility_AMD'] = (data2['High'] - data2['Low']) / data2['Open']

plt.figure(figsize=(8, 5))
plt.plot(data1.index, data1['Volatility_NVDA'], label='NVDA Volatility', color='royalblue', linewidth=2)
plt.plot(data2.index, data2['Volatility_AMD'], label='AMD Volatility', color='darkorange', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Intra-day Volatility (% of Open)')
plt.title('Intra-day Volatility of NVDA and AMD (YTD)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("plots/volatility.png", dpi=300)
plt.show()
