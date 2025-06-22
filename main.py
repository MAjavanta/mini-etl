from etl.load import load_csv_with_null_rows


def main():
    print("Hello from mini-etl!")


if __name__ == "__main__":
    # main()
    df = load_csv_with_null_rows("Sample_data.csv")
    print(df.shape)
