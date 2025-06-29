from etl.extract import load_csv_with_null_rows
from etl.load import write_to_file
from etl.transform import drop_columns, drop_empty_columns


def main():
    print("Hello from mini-etl!")


if __name__ == "__main__":
    # main()
    df = load_csv_with_null_rows("Sample_data.csv")
    df = drop_columns(df)
    df = drop_empty_columns(df)
    # write_to_file(df, "Clean_data.csv")
    print(df.shape)
    print(type(df))
