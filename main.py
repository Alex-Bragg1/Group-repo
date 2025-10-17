import os
import pandas as pd
import GROUPMODULE.Plot as stock_plot
import GROUPMODULE.stock_statistics as stock_stats

def main():   
    AMD_csv_path = os.path.join("GROUPMODULE", "AMD_2025.csv")
    NVDA_csv_path = os.path.join("GROUPMODULE", "NVDA_2025.csv")

    # Load CSV data
    AMD_data = pd.read_csv(AMD_csv_path, header=[0, 1], index_col=0, parse_dates=True)
    NVDA_data = pd.read_csv(NVDA_csv_path, header=[0, 1], index_col=0, parse_dates=True)

    # Print first 10 rows 
    print("AMD Data:")
    print(AMD_data.head(10))
    print("\nNVDA Data:")
    print(NVDA_data.head(10))

    # --- Summary statistics for AMD ---
    print("\n=== AMD Summary Statistics ===")
    AMD_summary_stats = stock_stats.basic_statistics(AMD_data['Close'])
    AMD_overall_pct_chng = stock_stats.overall_percentage_change(AMD_data['Close'])
    AMD_last_day_pct_chng = stock_stats.daily_percentage_change(AMD_data['Close'])

    print("Summary Stats:\n", AMD_summary_stats)
    print("Overall % Change:", AMD_overall_pct_chng)
    print("Last Day % Change:", AMD_last_day_pct_chng)

    # --- Plotting AMD and NVDA ---
    stock_plot.all_plot(AMD_data, NVDA_data)

if __name__ == "__main__":
    main()
