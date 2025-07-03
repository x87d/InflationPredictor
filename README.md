# World Bank Inflation Linear Regression Tool

A Python-based CLI tool to analyze inflation trends using **World Bank CPI (Consumer Price Index)** data and perform **linear regression** to model and predict inflation rates for any given country.

---

## 📌 Features

- Loads and cleans raw World Bank inflation data.
- Filters by user-specified **country name** and **year range**.
- Trains a **linear regression model** on historical inflation data.
- Outputs:
  - Regression formula
  - R² score
  - Coefficients
- Optionally predicts inflation rate for a future year.
- Visualizes:
  - Actual inflation data points
  - Fitted regression line
  - Predicted value (if requested)

---

## 📁 Dataset Used
    World Bank , Inflation, consumer prices (annual %).
    Accessed via: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG   
     
This project uses the following World Bank datasets:

1. **Inflation Data**: `API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_20380.csv`
2. **Country Metadata**: `Metadata_Country_API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_20380.csv`
3. **Indicator Metadata**: `Metadata_Indicator_API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_20380.csv`

These files should be placed in the same directory as the script.

---

## 🛠️ Requirements

Make sure you have the following Python libraries installed:

```bash
pip install pandas scikit-learn matplotlib
```

---

## 🧪 How to Use

1. Place the required CSV files in the project folder.
2. Run the script:

   ```bash
   python inflation_regression.py
   ```

3. Follow the prompts:

   - Enter a **country name** (e.g., "Lebanon", "United States")
   - Specify a **training year range** (e.g., 2000–2020)
   - Optionally, enter a **future year** to predict (e.g., 2025)

4. View the output:
   - Model summary printed in terminal
   - A plot showing actual vs predicted inflation trend

---




## ✅ Notes

- The script is robust against missing values and automatically skips years with no inflation data.
- It assumes the input CSVs are from the World Bank and follow their standard format.
- Designed for command-line use; no GUI or web interface needed.

---

