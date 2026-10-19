# ======================================================
# Experiment: Multiple Linear Regression (50 Startups)
# Stepwise Feature Selection & Performance Evaluation
# ======================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 支援 Jupyter Notebook display 與 終端機 print
try:
    from IPython.display import display
except ImportError:
    display = print

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 載入資料集
url = (
    "https://gist.githubusercontent.com/"
    "GaneshSparkz/b5662effbdae8746f7f7d8ed70c42b2d/"
    "raw/faf8b1a0d58e251f48a647d3881e7a960c3f0925/"
    "50_Startups.csv"
)
df = pd.read_csv(url)

print("Dataset Shape:", df.shape)
display(df.head())

# 2. 類別變數 One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["State"], drop_first=True, dtype=int)
X = df_encoded.drop(columns=["Profit"])
y = df_encoded["Profit"]

# 3. 切分訓練集與測試集 (test_size=0.20, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# 4. 逐步特徵加入序列
feature_steps = [
    ["R&D Spend"],
    ["R&D Spend", "Marketing Spend"],
    ["R&D Spend", "Marketing Spend", "State_New York"],
    ["R&D Spend", "Marketing Spend", "State_New York", "State_Florida"],
    ["R&D Spend", "Marketing Spend", "State_New York", "State_Florida", "Administration"]
]

display_labels = [
    ["R&D Spend"],
    ["R&D Spend", "Marketing Spend"],
    ["R&D Spend", "Marketing Spend", "State_New York"],
    ["R&D Spend", "Marketing Spend", "State_New York", "State_Florida"],
    ["R&D Spend", "Marketing Spend", "State_New York", "State_Florida", "State_California"]
]

# 5. 訓練模型並評估 RMSE 與 R-squared
results = []
for i, features in enumerate(feature_steps):
    model = LinearRegression().fit(X_train[features], y_train)
    y_pred = model.predict(X_test[features])
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results.append({
        "Number of Features": i + 1,
        "Selected Features": display_labels[i],
        "RMSE": rmse,
        "R-squared": r2
    })

result_df = pd.DataFrame(results)

print("\nModel Evaluation Table:")
display(result_df)

# 6. 繪製精確重現附圖之圖表
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左圖：RMSE by Number of Features
axes[0].plot(
    result_df["Number of Features"],
    result_df["RMSE"],
    marker="o",
    color="#3b75af",
    linewidth=1.8,
    markersize=6
)
axes[0].set_title("RMSE by Number of Features", fontsize=12)
axes[0].set_xlabel("Number of Features", fontsize=10)
axes[0].set_ylabel("RMSE", fontsize=10)

# 右圖：R-squared by Number of Features
axes[1].plot(
    result_df["Number of Features"],
    result_df["R-squared"],
    marker="o",
    color="#3b75af",
    linewidth=1.8,
    markersize=6
)
axes[1].set_title("R-squared by Number of Features", fontsize=12)
axes[1].set_xlabel("Number of Features", fontsize=10)
axes[1].set_ylabel("R-squared", fontsize=10)

plt.tight_layout()

# 儲存圖形檔案供查看
plt.savefig("experiment_result.png", dpi=300)
print("\n圖形已儲存為 experiment_result.png")

plt.show()
