# ======================================================
# HW2: Multiple Linear Regression (WHO Life Expectancy)
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

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 載入資料集
# 使用本機快取或公開遠端 URL
csv_path = "Life_Expectancy_Data.csv"
try:
    df = pd.read_csv(csv_path)
except Exception:
    url = "https://raw.githubusercontent.com/as927097/STA321/main/Life%20Expectancy%20Data.csv"
    df = pd.read_csv(url)

# 清理欄位名稱頭尾空白
df.columns = df.columns.str.strip()

print("=" * 60)
print("HW2: WHO Life Expectancy 多元線性迴歸特徵選擇與評估")
print("=" * 60)
print("\n原始資料集維度:", df.shape)

# 2. 指定目標變數與題目要求之 8 個特徵
target_col = "Life expectancy"
feature_cols = [
    "Schooling",          # 教育年數
    "Adult Mortality",    # 成人死亡率
    "Polio",              # 小兒麻痺疫苗接種率
    "BMI",                # 身體質量指數
    "GDP",                # 人均國內生產毛額
    "Alcohol",            # 人均純酒精攝取量
    "Hepatitis B",        # B型肝炎疫苗接種率
    "Total expenditure"   # 醫療保健支出佔政府支出百分比
]

# 排除目標變數缺失之觀測值
df = df.dropna(subset=[target_col])

# 3. 遺漏值補齊 (以國家中位數補齊，若該國全缺則以全域中位數填補)
for col in feature_cols:
    df[col] = df.groupby("Country")[col].transform(lambda x: x.fillna(x.median()))
    df[col] = df[col].fillna(df[col].median())

X = df[feature_cols]
y = df[target_col]

print("\n清理後有效筆數:", len(df))
print("納入自變數特徵 (8項):")
for idx, col in enumerate(feature_cols, 1):
    print(f"  {idx}. {col}")

# 4. 切分訓練集與測試集 (test_size=0.20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

cv = KFold(n_splits=5, shuffle=True, random_state=42)

# 5. 逐步特徵加入序列 (Forward Stepwise Selection)
selected_features = []
remaining_features = list(feature_cols)
experiment_rows = []

for k in range(1, len(feature_cols) + 1):
    best_candidate = None
    best_cv_rmse = float("inf")

    # 挑選使 5-Fold CV RMSE 最低的特徵
    for candidate in remaining_features:
        trial_subset = selected_features + [candidate]
        model = LinearRegression()
        cv_scores = cross_val_score(
            model,
            X_train[trial_subset],
            y_train,
            scoring="neg_mean_squared_error",
            cv=cv
        )
        cv_rmse = np.sqrt(-cv_scores.mean())
        if cv_rmse < best_cv_rmse:
            best_cv_rmse = cv_rmse
            best_candidate = candidate

    selected_features.append(best_candidate)
    remaining_features.remove(best_candidate)

    # 以選出之 k 個特徵訓練最終模型並於測試集評估
    final_model = LinearRegression()
    final_model.fit(X_train[selected_features], y_train)
    y_pred = final_model.predict(X_test[selected_features])

    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    test_r2 = r2_score(y_test, y_pred)

    experiment_rows.append({
        "Number of Features": k,
        "Added Feature": best_candidate,
        "Selected Features": list(selected_features),
        "CV RMSE": best_cv_rmse,
        "RMSE": test_rmse,
        "R-squared": test_r2
    })

result_df = pd.DataFrame(experiment_rows)

print("\n" + "=" * 60)
print("特徵選擇與模型評估結果彙總表:")
print("=" * 60)
display(result_df[["Number of Features", "Added Feature", "RMSE", "R-squared", "CV RMSE"]].round(4))

# 6. 繪製圖形 (完全比照 main.py 之左右雙子圖風格)
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

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
axes[0].set_ylabel("RMSE (Years)", fontsize=10)
axes[0].set_xticks(range(1, len(feature_cols) + 1))

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
axes[1].set_xticks(range(1, len(feature_cols) + 1))

plt.tight_layout()

# 儲存圖形檔案
plt.savefig("hw2_result.png", dpi=300)
print("\n圖形已成功儲存為 hw2_result.png")

plt.show()
