# Machine Learning Regression Explorer 🚀

> 中興大學 人工智慧與資安 (L07 50 Startup LR / HW2 WHO Life Expectancy / Boston Housing)  
> 多元線性迴歸特徵探索、模型評估與即時數值預測互動式 Web 平台

🔗 **GitHub Pages 線上展示網址**：[https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/)

---

## 📌 支援三大資料集 (透過網頁最上方導覽列切換)

本平台在**網頁最頂部**提供即時切換下拉選單，支援三大經典機器學習迴歸資料集：

### 1. 🏢 50 Startups (新創獲利預測)
* **目標變數**：`Profit` (淨獲利，美元)
* **特徵 (5 項)**：`R&D Spend`、`Administration`、`Marketing Spend`、`State_Florida`、`State_New York`
* **模型評估**：
  * $k=2$（R&D + Marketing）達到最低 RMSE `$8,198.80`，解釋力 $R^2 = 94.74\%$。
* **對應程式**：`main.py`

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
* **對應程式**：`hw2.py`

### 3. 🏡 Boston Housing (波士頓房價中位數預測)
* **目標變數**：`MEDV` (房價中位數，千美元 / $1,000s)
* **特徵 (8 項)**：
  1. `CRIM`（城鎮人均犯罪率）
  2. `RM`（平均房間數）
  3. `AGE`（1940年前建造的老屋比例）
  4. `NOX`（一氧化氮濃度/空氣污染）
  5. `DIS`（到五大就業中心距離）
  6. `TAX`（全額房產稅率）
  7. `PTRATIO`（城鎮小學師生比例）
  8. `LSTAT`（社經地位較低人口比例）
* **模型評估**：
  * $k=5$ 納入 `LSTAT, RM, PTRATIO, DIS, NOX` 時達到測試集最低 RMSE $5.020$（約 $\$5,020$ 美元），$R^2 = 65.64\%$。
* **對應程式**：`DICBoston.py`

---

## 💻 專案檔案結構

* `index.html`：多資料集互動式 Web 入口頁面（頂端整合資料集切換導覽列）
* `style.css`：現代化響應式 UI 樣式表（還原 50 Startups 高質感簡潔風格）
* `app.js`：前端互動邏輯、三大資料集切換、動態 $k$ 特徵按鈕、Chart.js 圖表渲染、即時模擬預測
* `main.py`：50 Startups 多元線性迴歸實作腳本
* `hw2.py`：WHO Life Expectancy 多元線性迴歸與逐步特徵選擇實作腳本
* `DICBoston.py`：Boston Housing 多元線性迴歸與逐步特徵選擇實作腳本
* `experiment_result.png`：50 Startups 評估結果圖表
* `hw2_result.png`：WHO Life Expectancy 評估結果圖表
* `boston_result.png`：Boston Housing 評估結果圖表
* `Life_Expectancy_Data.csv`：WHO 全球 193 國健康與經濟原始資料
* `BostonHousing.csv`：波士頓 506 區房價原始資料

---

## 🚀 本地執行方式

### 1. 執行各作業 Python 分析腳本
```bash
# 50 Startups 獲利分析
python main.py

# WHO 預期壽命分析 (HW2)
python hw2.py

# Boston 房價分析
python DICBoston.py
```

### 2. 開啟互動式三大資料集網站
直接在瀏覽器雙擊開啟 `index.html`，或使用 Python 伺服器：
```bash
python -m http.server 8080
```
在瀏覽器造訪 `http://localhost:8080`。

---

## 🌐 GitHub Pages 部署

本專案支援純靜態託管：
1. 進入儲存庫設定：[https://github.com/sudi811/1019-50Start/settings/pages](https://github.com/sudi811/1019-50Start/settings/pages)
2. 在 **Branch** 選取 `main` / `/(root)` 並點擊 **Save**。
3. 即可在 [https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/) 線上操作！