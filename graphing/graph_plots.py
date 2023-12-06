import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data copy-pasted from running our models
base = [12.2061, 13.4204, 12.4518, 12.5703, 12.4213, 11.9246, 13.1907, 11.9657, 12.1694, 12.1512]
finetuned = [10.9246, 12.1907, 10.9657, 11.1694, 11.1512, 11.2061, 12.4204, 11.4518, 11.5703, 12.4213]

# Creating a DataFrame
data = {'Model': ['finetuned']*len(finetuned) + ['base']*len(base),
        'Value': finetuned + base}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 6))
sns.stripplot(data=df, x='Model', y='Value', palette='Set2')

average_values = df.groupby('Model')['Value'].median().reset_index()
sns.pointplot(data=average_values, x='Model', y='Value', color='red', join=False, markers='D')

plt.title('Perplexity of Zero-Shot Validation on Finetuned and Base Models')
plt.show()
