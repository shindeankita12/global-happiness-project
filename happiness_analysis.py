import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Country': ['Norway', 'Denmark', 'Iceland', 'Switzerland', 'Finland', 'Netherlands', 'Canada', 'New Zealand', 'Australia', 'Sweden'],
    'Happiness Score': [7.54, 7.60, 7.49, 7.49, 7.63, 7.38, 7.32, 7.31, 7.28, 7.28],
    'GDP per Capita': [1.62, 1.58, 1.48, 1.52, 1.54, 1.50, 1.48, 1.40, 1.48, 1.51],
    'Social Support': [1.52, 1.55, 1.52, 1.52, 1.58, 1.52, 1.52, 1.48, 1.52, 1.50],
    'Healthy Life Expectancy': [0.96, 0.97, 0.95, 1.00, 0.96, 0.94, 0.95, 0.95, 0.95, 0.95]
}

df = pd.DataFrame(data)

# Correlation heatmap
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.heatmap(df.drop(columns='Country').corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Happiness Factors")
plt.tight_layout()
plt.show()

# Scatter plots
def plot_scatter(x, y):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f"{y} vs {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()

plot_scatter('GDP per Capita', 'Happiness Score')
plot_scatter('Social Support', 'Happiness Score')
plot_scatter('Healthy Life Expectancy', 'Happiness Score')