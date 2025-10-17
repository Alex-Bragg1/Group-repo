# GroupModule

A Python package designed to **plot stock prices for AMD and NVDA** and create **summary statistics** for their price data.

**IMPORTANT:**  
- Can use EITHER testing.ipynb or main.py to run the package
- To run the testing notebook or scripts, run them **outside of the package folder**.

---

## Features

### `Plot.py`
**Function:** `all_plot(data1, data2)`  

- Plots **closing prices** of AMD vs NVDA  
- Plots **trade volumes** of AMD vs NVDA  
- Plots **intra-day volatility** of AMD vs NVDA  

### `stock_statistics.py`
- **`basic_statistics(vector)`**  
  Returns a dictionary of summary statistics for a numeric vector (e.g., AMD Close price).

- **`overall_percentage_change(vector)`**  
  Returns the overall percentage change for a numeric vector (e.g., AMD Close price).

- **`daily_percentage_change(vector)`**  
  Returns the percentage change for the **last day** for a numeric vector (e.g., AMD Close price).

---

## Folder Structure
Clone the repository: git clone https://github.com/Alex-Bragg1/Group-repo.git



