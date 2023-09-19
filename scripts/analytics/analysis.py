import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis, shapiro
import faker as Faker

df = pd.read_csv('https://raw.githubusercontent.com/daniloui001/datasci_3_eda/main/processed/IHME_PREM_CH_HEALTH_2021_Y2021M09D14.CSV.CSV')
df.columns