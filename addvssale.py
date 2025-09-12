import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# -----------------------------
# Linear function: Sales = m*AdSpending + c
# -----------------------------

m = 0.5   # slope (e.g., 0.5 customers per $1)
c = 50    # base sales when no ads are spent

# Generate Ad spending data (from $0 to $2000)
ad_spending = np.linspace(0, 2000, 50)

# Calculate sales with some random noise
sales = m * ad_spending + c + np.random.normal(0, 20, size=ad_spending.shape)
# -----------------------------
# Plot using seaborn
# -----------------------------
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))

# Scatter plot of data
sns.scatterplot(x=ad_spending, y=sales, color="blue", s=60, label="Observed Data")

# Plot the true linear function
true_sales = m * ad_spending + c
sns.lineplot(x=ad_spending, y=true_sales, color="red", label="True Relationship")

plt.title("Advertising Spending vs Sales", fontsize=14)
plt.xlabel("Ad Spending ($)", fontsize=12)
plt.ylabel("Sales (Customers)", fontsize=12)
plt.legend()
plt.show()