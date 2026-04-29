import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.cm as cm
import statsmodels.formula.api as smf
import seaborn as sns
os.makedirs("graphs", exist_ok=True)

print('Loading SUDORS-Fatal-Overdose-Data.csv...')
sudors = pd.read_csv("SUDORS-Fatal-Overdose-Data.csv")
display(sudors.head())

print('\nLoading naloxone_dispensing_rates.csv...')
naloxone = pd.read_csv("naloxone_dispensing_rates.csv")
display(naloxone.head())

print('\nLoading Opioid_Crime.csv...')
opioid_crime = pd.read_csv("Opioid_Crime.csv")
display(opioid_crime.head())

print('\nLoading filtered_nsduh.csv...')
nsduh = pd.read_csv("filtered_nsduh.csv", low_memory=False)
display(nsduh.head())
