from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# ---- Step 1: Create dataset ----
data = {
    "Size": [500, 800, 1000, 1200, 1500, 1800, 2000],   # X (Independent variable)
    "Price": [150000, 200000, 250000, 280000, 340000, 400000, 430000]  # y (Dependent variable)
}

df = pd.DataFrame(data)   # <-- yeh line zaroori hai

# ---- Step 2: Define X and y ----
X = df[["Size"]]   # Features
y = df["Price"]    # Target

# ---- Step 3: Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Step 4: Train model ----
model = LinearRegression()
model.fit(X_train, y_train)

# ---- Step 5: Predict ----
y_pred = model.predict(X_test)

# ---- Step 6: Evaluate ----
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R²:", r2)
