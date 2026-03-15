# Required Libraries Install
    # pip install pandas scikit-learn

# CSV Load
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("students.csv")

print(df.head())


# Features aur Target Split
X = df[["hours_studied", "sleep_hours"]]
y = df["exam_score"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Train
model = LinearRegression()
model.fit(X_train, y_train)


# Prediction
new_data = pd.DataFrame({
    "hours_studied": [12],
    "sleep_hours": [12]
})
prediction = model.predict(new_data)
print("Predicted Score:", prediction)