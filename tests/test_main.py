from etl.load import load_csv_with_null_rows


def test_load_csv_with_null_rows():
    df = load_csv_with_null_rows("Sample_data.csv")
    assert not df.empty
