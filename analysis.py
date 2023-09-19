import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis, shapiro
import faker as Faker

df = pd.read_csv('https://raw.githubusercontent.com/daniloui001/datasci_3_eda/main/processed/us_census.csv')
###print(df.columns)

print(df['AGE'])
print(df.dtypes)

print(df.AGE.describe())