### This is a python package designed to plot stock prices for AMD and NVDA and create some summary statisitcs. 
### IMPORTANT:
- To run the testing notebook run this outside of the package!!!!

Plot.py:
all_plots function:
- Plots prices of AMD vs NVDA
- Plots trade volumes of AMD vs NVDA
- Plots intra-day volatility of AMD vs NVDA


stock_statistics.py:
basic_statistics function:
- Returns dict of summary statistics for a vector of your choice i.e. AMD Close price
overall_percentage_change function:
- Returns overall percentage change for a vector of your choice i.e. AMD Close price
daily_percentage_change function:
- Returns daily price change for the last day for a vector of your choice i.e. AMD Close price


my_module/
├── __init__.py
├── AMD_2025.csv
├── NVDA.csv
├── plot.py
├── stock_statistics.py
├── README.md
└── requirements.txt

Clone the repository: git clone https://github.com/Alex-Bragg1/Group-repo.git



