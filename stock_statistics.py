### 
## Statistics for stock market data
### 

import numpy as np

def basic_statistics(data):
    """
    Calculate basic statistics for stock market data.

    Returns:
    dict: A dictionary containing mean, median, variance, and standard deviation.
    """
    if len(data) == 0:
        raise ValueError("Data list is empty")

    data = np.array(data)
    
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)

    return {
        'mean': mean,
        'median': median,
        'variance': variance,
        'std_dev': std_dev
    }


def overall_percentage_change(data):
    """
    Calculate the overall percentage change from the first to the last two stock points.
    """
    
    data = np.array(data)
    
    return (data[-1] - data[0]) / data[0] * 100 if len(data) > 1 else 0

def daily_percentage_change(data):
    """
    Calculate the daily percentage change from the last two stock points.
    """
    
    data = np.array(data) 
    
    return (data[-1] - data[-2]) / data[-2] * 100 if len(data) > 1 else 0
