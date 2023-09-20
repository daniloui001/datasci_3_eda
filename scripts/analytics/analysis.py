import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis, shapiro, zscore
import faker as Faker
import seaborn as sns
from pandas_profiling import ProfileReport

df = pd.read_csv('https://raw.githubusercontent.com/daniloui001/datasci_3_eda/main/processed/us_census.csv')
### print(df.columns)

print(df['AGE'])
print(df.dtypes)

print(df.AGE.describe())

plt.hist(df['AGE'], bins=5, color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('US Census Age Distribution')
plt.show()

### Scatter Plot// POSITIVE CORRELATION FOUND

plt.figure(figsize=(8, 6))
sns.scatterplot(x=range(len(df['AGE'])), y=df['AGE'])
plt.xlabel('Age')
plt.ylabel('Frequency of Age')
plt.title("Scatter Plot of Age Distribution")
plt.show()

z_scores = zscore(df['AGE'])
threshold = 2
outliers = np.where(np.abs(z_scores) > threshold)
outlier_values = [df['AGE'][i] for i in outliers[0]]

print("Outlier Indices in Array:", outliers)
print("Outlier Values:", outlier_values)

### Correlational Coefficient

correlation_coefficient = df['AGE'].corr(df['AGE'])

print("Correlation Coefficient:", correlation_coefficient)

### Identifying Outliers using IQR method 

q1 = np.percentile(df['AGE'], 25)
q3 = np.percentile(df['AGE'], 76)
iqr = q3 - q1

threshold_lower = q1 - 1.5 * iqr
threshold_upper = q3 + 1.5 * iqr

# Identify outliers
outliers1 = [x for x in df['AGE'] if x < threshold_lower or x > threshold_upper]

print("Outliers:", outliers1)


### Creating automated Report


df1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK3/data/trinetx/lab_result.csv')

report = ProfileReport(df1)
report.to_file('processed/us_census_report.html')