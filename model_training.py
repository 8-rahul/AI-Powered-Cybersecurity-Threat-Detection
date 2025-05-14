import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("Sample_Dataset.csv")

# Display first five rows
print(data.head())

# Drop unnecessary columns
data = data.drop(["timestamp"], axis=1)

# Normalize numerical values
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.drop("threat_label", axis=1))

# Split features and target
X = data.drop(columns=["threat_label"], errors='ignore')
y = data["threat_label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model,"cybersecurity_model.pkl")
print(f"Model saved as cybersecurity_model.pkl")