# Machine Learning Regression Explorer 🚀

> 中興大學 人工智慧與資安 (L07 50 Startup LR & HW2 WHO Life Expectancy)  
> 多元線性迴歸特徵探索、模型評估與即時數值預測互動式 Web 平台

🔗 **GitHub Pages 線上展示網址**：[https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/)

---

## 📌 支援雙資料集 (透過下拉選單切換)

本平台可透過頂部的 **「選擇分析資料集 (Select Dataset)」** 下拉選單即時無縫切換兩大機器學習資料集：

### 1. 🏢 50 Startups (新創獲利預測)
* **目標變數**：`Profit` (淨獲利，美元)
* **特徵 (5 項)**：`R&D Spend`、`Administration`、`Marketing Spend`、`State_Florida`、`State_New York`
* **模型評估**：
  * $k=2$（R&D + Marketing）達到最低 RMSE `$8,198.80`，解釋力 $R^2 = 94.74\%$。

### 2. 🌍 WHO Life Expectancy (全球預期壽命預測)
* **目標變數**：`Life expectancy` (平均預期壽命，歲)
* **特徵 (8 項)**：
  1. `Schooling`（教育年數）
  2. `Adult Mortality`（成人死亡率）
  3. `Polio`（小兒麻痺疫苗接種率）
  4. `BMI`（身體質量指數）
  5. `GDP`（人均國內生產毛額）
  6. `Alcohol`（純酒精年人均攝取量）
  7. `Hepatitis B`（B型肝炎疫苗接種率）
  8. `Total expenditure`（醫療保健支出佔比）
* **模型評估**：
  * 逐步特徵加入順序中，$k=7$ 特徵時達到 5-Fold CV 泛化誤差最低（$4.94$ 歲），測試集 $R^2 = 76.32\%$。

---

## 💻 專案檔案結構

* `index.html`：多資料集互動式 Web 入口頁面（包含資料集切換選單）
* `style.css`：現代化響應式 UI 樣式表
* `app.js`：前端互動邏輯、雙資料集即時切換、Chart.js 圖表渲染、即時模擬預測
* `main.py`：50 Startups 多元線性迴歸實作腳本
* `hw2.py`：WHO Life Expectancy 多元線性迴歸與特徵選擇實作腳本
* `experiment_result.png`：50 Startups 評估結果圖表
* `hw2_result.png`：WHO Life Expectancy 評估結果圖表
* `Life_Expectancy_Data.csv`：WHO 全球 193 國健康與經濟原始資料

---

## 🚀 本地執行方式

### 1. 執行 50 Startups 迴歸分析
```bash
python main.py
```

### 2. 執行 WHO Life Expectancy 迴歸分析 (HW2)
```bash
python hw2.py
```

### 3. 開啟互動式雙資料集網站
直接在瀏覽器雙擊開啟 `index.html`，或使用 Python 伺服器：
```bash
python -m http.server 8080
```
造訪 `http://localhost:8080`。

---

## 🌐 GitHub Pages 部署

本專案支援純靜態託管：
1. 進入儲存庫設定：[https://github.com/sudi811/1019-50Start/settings/pages](https://github.com/sudi811/1019-50Start/settings/pages)
2. 在 **Branch** 選取 `main` / `/(root)` 並點擊 **Save**。
3. 即可隨時在 [https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/) 線上操作！