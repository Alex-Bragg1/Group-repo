# main.py
# =============================
# Group Project Demo - Scientific Python App
# Date: 18 October 2025
# Demonstrates integration of the stock statistics and plotting modules.
# The app loads AMD and NVDA stock data, computes key statistics, 
# correlation, and generates visualizations using Matplotlib.
# =============================

import pandas as pd
import numpy as np
from my_module.stock_statistics import (
    basic_statistics,
    overall_percentage_change,
    daily_percentage_change,
)
import my_module.Plot as Plot


def load_stock_data(file_path):
    """Load stock CSV and return closing prices as a NumPy array."""
    df = pd.read_csv(file_path, skiprows=3)  # Skip first 3 non-data rows
    return df["Close"].values


def correlation(data1, data2):
    """Compute Pearson correlation between two stock price arrays."""
    return np.corrcoef(data1, data2)[0, 1]


def main():
    print("\n=== STOCK STATISTICS DEMO ===")

    # Load stock data
    amd_data = load_stock_data("my_module/AMD_2025.csv")
    nvda_data = load_stock_data("my_module/NVDA_2025.csv")

    # Compute statistics
    amd_stats = basic_statistics(amd_data)
    nvda_stats = basic_statistics(nvda_data)
    corr = correlation(amd_data, nvda_data)

    # Display statistics
    print("\n📊 AMD Statistics:")
    for k, v in amd_stats.items():
        print(f"{k.capitalize()}: {v:.2f}")

    print("\n📈 NVDA Statistics:")
    for k, v in nvda_stats.items():
        print(f"{k.capitalize()}: {v:.2f}")

    print(f"\n🔗 Correlation between AMD & NVDA: {corr:.3f}")

    # Additional insights
    print(f"\nAMD overall change: {overall_percentage_change(amd_data):.2f}%")
    print(f"NVDA overall change: {overall_percentage_change(nvda_data):.2f}%")
    print(f"AMD daily change (last day): {daily_percentage_change(amd_data):.2f}%")
    print(f"NVDA daily change (last day): {daily_percentage_change(nvda_data):.2f}%")

    # Run plots
    print("\n📊 Generating visualizations...")
    Plot  # Automatically runs and shows all plots


if __name__ == "__main__":
    main()
