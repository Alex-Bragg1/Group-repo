# Zavier and Freddie Branch
# Date Created: 16 - 10 - 2025
# Last Modified: 17 - 10 - 2025
# Description: Comparison of Nvidia and Advanced Micro Devices using plots - 
#              These are two computer chip companies

# Importing libraries required
import matplotlib.pyplot as plt


def all_plot(AMD_data, NVDA_data):
    """
    Plots Closing Prices, Trade Volumes, and Intra-day Volatility
    for AMD and NVDA (multi-index columns).
    """

    # Hard-coded stock names (second level of multi-index)
    stock_AMD = 'AMD'
    stock_NVDA = 'NVDA'

    # --- FIGURE 1: Closing Prices ---
    plt.figure(figsize=(10,5))
    plt.plot(AMD_data.index, AMD_data[('Close', stock_AMD)], label='Close AMD')
    plt.plot(NVDA_data.index, NVDA_data[('Close', stock_NVDA)], label='Close NVDA')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Closing Prices Comparison')
    plt.xticks(rotation=45)
    plt.legend()

    # --- FIGURE 2: Trade Volumes ---
    plt.figure(figsize=(10,5))
    plt.plot(AMD_data.index, AMD_data[('Volume', stock_AMD)], label='Volume AMD')
    plt.plot(NVDA_data.index, NVDA_data[('Volume', stock_NVDA)], label='Volume NVDA')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Trade Volumes Comparison')
    plt.xticks(rotation=45)
    plt.legend()

    # --- FIGURE 3: Intra-day Volatility ---
    AMD_data[('Volatility', stock_AMD)] = (AMD_data[('High', stock_AMD)] - AMD_data[('Low', stock_AMD)]) / AMD_data[('Open', stock_AMD)]
    NVDA_data[('Volatility', stock_NVDA)] = (NVDA_data[('High', stock_NVDA)] - NVDA_data[('Low', stock_NVDA)]) / NVDA_data[('Open', stock_NVDA)]

    plt.figure(figsize=(10,5))
    plt.plot(AMD_data.index, AMD_data[('Volatility', stock_AMD)], label='Volatility AMD')
    plt.plot(NVDA_data.index, NVDA_data[('Volatility', stock_NVDA)], label='Volatility NVDA')
    plt.xlabel('Date')
    plt.ylabel('Intra-day Volatility')
    plt.title('Intra-day Volatility Comparison')
    plt.xticks(rotation=45)
    plt.legend()

    plt.show()
