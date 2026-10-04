import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset/students.csv")

print("\n===== DATASET INFORMATION =====")
print(data.info())

print("\n===== FIRST 5 ROWS =====")
print(data.head())

print("\n===== STATISTICS =====")
print(data.describe())

print("\n===== MISSING VALUES =====")
print(data.isnull().sum())


# -----------------------------
# 1. Placement Distribution
# -----------------------------

plt.figure(figsize=(6, 4))

sns.countplot(
    x="placed",
    data=data
)

plt.title("Placement Distribution")
plt.xlabel("Placement (0 = No, 1 = Yes)")
plt.ylabel("Number of Students")

plt.savefig("placement_distribution.png")
plt.show()


# -----------------------------
# 2. Study Hours vs Placement
# -----------------------------

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="placed",
    y="study_hours",
    data=data
)

plt.title("Study Hours vs Placement")
plt.xlabel("Placement")
plt.ylabel("Study Hours")

plt.savefig("study_hours_vs_placement.png")
plt.show()


# -----------------------------
# 3. Attendance vs Placement
# -----------------------------

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="placed",
    y="attendance",
    data=data
)

plt.title("Attendance vs Placement")
plt.xlabel("Placement")
plt.ylabel("Attendance (%)")

plt.savefig("attendance_vs_placement.png")
plt.show()


# -----------------------------
# 4. Correlation Heatmap
# -----------------------------

plt.figure(figsize=(8, 6))

correlation = data.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")

plt.savefig("correlation_heatmap.png")
plt.show()


print("\nAnalysis completed successfully!")