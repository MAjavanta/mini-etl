import csv
import pandas as pd


def load_csv_with_null_rows(data_file):
    with open(data_file, "r", encoding="cp1252") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if any(cell.strip() for cell in row):
                header_row_index = i
                break
        else:
            raise ValueError("No rows with data found")

    df = pd.read_csv(
        data_file,
        header=header_row_index,
        encoding="cp1252",
        low_memory=False,
    )
    df = df.dropna(how="all")
    return df
