import zipfile
import os
import pandas as pd
from urllib.request import urlretrieve
from sqlalchemy import create_engine,FLOAT, BIGINT, TEXT

# Define the download URL and file names
download_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_file_name = "mowesta-dataset.zip"
extracted_folder = "mowesta-dataset"

def load_and_transform_data(csv_url: str) -> pd.DataFrame:

    # Download ZIP file
    urlretrieve(download_url, zip_file_name)

    # Extract CSV from ZIP
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extract('data.csv', extracted_folder)


    # Define the columns to keep and their new names
    columns_to_keep = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
    new_column_names = {"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"}

    # Load data into a DataFrame
    data_path = os.path.join(extracted_folder, "data.csv")
    df = pd.read_csv((data_path),sep=';',index_col=False, decimal=',',usecols=columns_to_keep)

    # Reshape data
    df = df[columns_to_keep].rename(columns=new_column_names)

    # Transform data (Celsius to Fahrenheit)
    df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
    df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

    # Validate data
    # Example validation: Geraet should be an id over 0
    df = df[df["Geraet"] > 0]
    df = df[df['Monat'].isin(range(1, 13))]
    df = df[df['Temperatur'].between(-459.67, 212)]
    df = df[df['Batterietemperatur'].between(-459.67,212)]
    df = df[df['Geraet aktiv'].isin(['Ja', 'Nein'])]

    return df

# Write data to SQLite database
def write_to_sqlite(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    engine = create_engine(f"sqlite:///{database_name}")
    types={
        'Geraet': BIGINT,
        'Hersteller': TEXT,
        'Model': TEXT,
        'Monat': BIGINT,
        'Temperatur': FLOAT,
        'Batterietemperatur': FLOAT,
        'Geraet aktiv': TEXT
    }
    df.to_sql(table_name, con=engine, index=False, if_exists='replace', dtype=types)

    print('Datapipeline finished successfully')
    print(f'Data is stored in table "{table_name}" in database "{database_name}"')

if __name__ == "__main__":
    data = load_and_transform_data(download_url)
    write_to_sqlite(data, "temperatures.sqlite", "temperatures")