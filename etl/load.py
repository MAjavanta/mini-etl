def write_to_file(df, filepath):
    df.to_csv(filepath, index=False)
