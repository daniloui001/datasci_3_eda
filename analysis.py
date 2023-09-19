import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis, shapiro
import faker as Faker

df = pd.read_csv('https://raw.githubusercontent.com/daniloui001/datasci_3_eda/main/processed/IHME.CSV')
###print(df.columns)

print(df['country'])
print(df.dtypes)

print(df.country.describe())