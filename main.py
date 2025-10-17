import GROUPMODULE.Plot as stock_plot
import GROUPMODULE.stock_statistics as stock_stats
import os
import pandas as pd


AMD_csv_path = os.path.join("GROUPMODULE", "AMD_2025.csv")
NVDA_csv_path = os.path.join("GROUPMODULE", "NVDA_2025.csv")
AMD_data = pd.read_csv(AMD_csv_path)
NVDA_data = pd.read_csv(NVDA_csv_path)

print(AMD_data.head())

stock_plot.all_plot(AMD_data, NVDA_data)
AMD_close_mean = stock_stats.basic_statistics(AMD_data['Close'][0])



