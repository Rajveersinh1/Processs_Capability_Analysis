# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Set specification limits
target = 5
LSL = 3
USL = 7

# Generate normally distributed data points
data = np.random.normal(loc=target,scale=1,size=100)

# Calculate Cp
Cp = (USL-LSL)/(6*np.std(data))

# Calculate Cpk
Cpk = min((USL-data.mean())/(3*data.std()), (data.mean()-LSL)/(3*data.std()))

# Calculate z-value
z = min((USL-data.mean())/(data.std()), (data.mean()-LSL)/(data.std()))

# Get data summary statistics
num_samples = len(data)
sample_mean = data.mean()
sample_std = data.std()
sample_max = data.max()
sample_min = data.min()
sample_median = np.median(data)

# Get percentage of data points outside of specification limits
pct_below_LSL = len(data[data < LSL])/len(data)*100
pct_above_USL = len(data[data > USL])/len(data)*100

# Write .txt file with results
with open('process_results.txt', "w") as results:
    results.write("PROCESS CAPABILITY ANALYSIS\n")
    
    results.write("-----------------------------------\n")
    results.write(f"Specifications\n")
    results.write(f"\nTaget: {target}\n")
    results.write(f"LSL: {LSL}\n")
    results.write(f"USL: {USL}\n")    
    
    results.write("-----------------------------------\n")
    results.write(f"Indices\n")
    results.write(f"\nCp: {round(Cp,2)}\n")
    results.write(f"Cpk: {round(Cpk,2)}\n")
    results.write(f"z: {round(z,2)}\n")
    
    results.write("-----------------------------------\n")
    results.write(f"Summary Statistics\n")
    results.write(f"\nNumber of samples: {round(num_samples,2)}\n")
    results.write(f"Sample mean: {round(sample_mean,2)}\n")
    results.write(f"Sample std: {round(sample_std,2)}\n")
    results.write(f"Sample max: {round(sample_max,2)}\n")
    results.write(f"Sample min: {round(sample_min,2)}\n")
    results.write(f"Sample median: {round(sample_median,2)}\n")
    
    results.write(f"Percentage of data points below LSL: {round(pct_below_LSL,2)}%\n")
    results.write(f"Percentage of data points above USL: {round(pct_above_USL,2)}%\n")