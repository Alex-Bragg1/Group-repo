# 
# Zavier and Freddie Branch
# Date Created: 16 - 10 - 2025
# Last Modified: 17 - 10 - 2025
# Description: Comparison of Nvidia and Advanced Micro Devices using plots - 
#              These are two computer chip companies

# Importing libraries required
import matplotlib.pyplot as plt
import yfinance as yf

# Downloading the dataset - NVDA = Nvidia, AMD = Advanced Micro Devices
data1 = yf.download("NVDA", start = "2025-01-01", end = "2025-09-15")
data2 = yf.download("AMD", start = "2025-01-01", end = "2025-09-15")

### FIGURE 1 - Plotting Close Prices Over Time for NVDA and AMD

# Creating first figure
plt.figure()

# Defining which data I want from the data set (Close Price)
plt.plot(data1.index, data1['Close'], label = 'Close Price NVDA')
plt.plot(data2.index, data2['Close'], label = 'Close Price AMD')

# Labelling x and y axis for the first figure (Close Price)
plt.xlabel('Date')
plt.ylabel('Price (USD)')

# Ensuring the dates are clear for figure 1
plt.xticks(rotation = 45)
plt.locator_params(axis = 'x', nbins=8)

# Creating a legend for clarity
plt.legend()

# Title of figure 1
plt.title('Comparing AMD and NVDA Closing Price YTD')   # YTD : Year to Date

### FIGURE 2 - Plotting Trade Volumes Over Time for NVDA and AMD

# Creating the second figure
plt.figure()

# Defining which data from the dataset is required (Volume)
plt.plot(data1.index, data1['Volume'], label = 'Volume NVDA')
plt.plot(data2.index, data2['Volume'], label = 'Volume AMD')

# Labelling the x and y axis
plt.xlabel('Date')
plt.ylabel('Volume')

# Title of the graph
plt.title('Trade Volumes of NVDA and AMD')

# Ensuring the dates are clear for figure 2
plt.xticks(rotation=45)
plt.locator_params(axis='x', nbins=8)

# Creating a legend for clarity
plt.legend()

# Calculations For Figure 3

# Pulling the High, Low, and Open prices from the dataset for NVDA
high_NVDA = data1['High']['NVDA']
low_NVDA = data1['Low']['NVDA']
open_NVDA = data1['Open']['NVDA']

# Pulling the High, Low, and Open prices from the dataset for NVDA
high_AMD = data2['High']['AMD']
low_AMD = data2['Low']['AMD']
open_AMD = data2['Open']['AMD']

# Calculate the intra-day volatility for NVDA
data1['Volatility NVDA'] = (high_NVDA - low_NVDA)/open_NVDA

# Calculate the intra-day volatility for AMD
data2['Volatility AMD'] = (high_AMD - low_AMD)/open_AMD

### FIGURE 3 - Plotting Intra-day Volatility Over Time for AMD and NVDA

# Defining a third figure showing intra-day volatiltiy
plt.figure()

# Plotting the volaility for both NVDA and AMD
plt.plot(data1.index, data1['Volatility NVDA'], label = 'Volatility NVDA')
plt.plot(data2.index, data2['Volatility AMD'], label = 'Volatility AMD')

# Labelling x and y axis for the third figure (Intra-day Volatility)
plt.xlabel('Date')
plt.ylabel('Intra-day Volatility (% of Open Px)')

# Creating a legend for clarity
plt.legend()

# Title of figure 3
plt.title('Intra-day Volatility of NVDA and AMD')

# Ensuring the dates are clear for figure 3
plt.xticks(rotation=45)
plt.locator_params(axis='x', nbins=8)

# Showing all figures / graphs
plt.show()

##