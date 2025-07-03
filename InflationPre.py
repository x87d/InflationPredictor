import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# Path to the CSV file
CSV_FILE = 'API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_20380.csv'

def load_and_clean_data(csv_file):
    # Read the CSV, skip metadata rows if present
    header_row = None
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        # Find the header row (starts with 'Country Name')
        for i, line in enumerate(f):
            if line.startswith('Country Name'):
                header_row = i
                break
    if header_row is None:
        raise ValueError("Could not find header row starting with 'Country Name' in the CSV file.")
    df = pd.read_csv(csv_file, skiprows=header_row)
    # Drop columns that are completely empty
    df = df.dropna(axis=1, how='all')
    # Set index to country name for easy lookup
    df.set_index('Country Name', inplace=True)
    return df

def get_country_list(df):
    return list(df.index)

def get_year_columns(df):
    # Year columns are those that are 4-digit numbers
    return [col for col in df.columns if col.isdigit()]

def plot_inflation(df, country):
    years = get_year_columns(df)
    data = df.loc[country, years].astype(float)
    # Drop missing values
    data = data.dropna()
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.values, marker='o', label='Historical Inflation')
    plt.title(f'Inflation Rate for {country}')
    plt.xlabel('Year')
    plt.ylabel('Inflation Rate (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    # Linear regression for prediction
    if len(data) > 1:
        X = np.array(data.index.astype(int)).reshape(-1, 1)
        y = data.values
        model = LinearRegression()
        model.fit(X, y)
        next_year = int(data.index[-1]) + 1
        pred = model.predict(np.array([[next_year]]))[0]
        plt.plot([data.index[-1], str(next_year)], [data.values[-1], pred], 'r--', label=f'Predicted {next_year}: {pred:.2f}%')
        plt.legend()
        print(f"Predicted inflation for {country} in {next_year}: {pred:.2f}%")
    else:
        print("Not enough data for prediction.")
    plt.tight_layout()
    plt.show()

def main():
    if not os.path.exists(CSV_FILE):
        print(f"CSV file '{CSV_FILE}' not found.")
        return
    df = load_and_clean_data(CSV_FILE)
    countries = get_country_list(df)
    print("Available countries:")
    for i, country in enumerate(countries):
        print(f"{i+1}. {country}")
    while True:
        choice = input("\nEnter country name (or number): ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(countries):
                country = countries[idx]
                break
            else:
                print("Invalid number. Try again.")
        elif choice in countries:
            country = choice
            break
        else:
            print("Country not found. Try again.")
    plot_inflation(df, country)

if __name__ == "__main__":
    main()
