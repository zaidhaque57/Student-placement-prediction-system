import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv("dataset/students.csv")

# Features
features = [
    "study_hours",
    "attendance",
    "assignment_score",
    "internal_marks",
    "previous_percentage"
]

X = data[features]
y = data["placed"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 40)
print("MODEL EVALUATION")
print("=" * 40)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# Confusion Matrix
# -----------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Not Placed", "Placed"],
    yticklabels=["Not Placed", "Placed"]
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.show()

# -----------------------------
# Feature Importance
# -----------------------------

importance = model.feature_importances_

feature_data = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

feature_data = feature_data.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_data)

plt.figure(figsize=(8, 5))

sns.barplot(
    x="Importance",
    y="Feature",
    data=feature_data
)

plt.title("Feature Importance")
plt.tight_layout()

plt.savefig("feature_importance.png")
plt.show()

# -----------------------------
# Save model
# -----------------------------

joblib.dump(model, "model/placement_model.pkl")

print("\nModel saved successfully!")