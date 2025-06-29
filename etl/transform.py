def drop_columns(df):
    df = df.drop(["objectTypeId", "EntityName", "EntityShortName"], axis=1)
    return df


def is_empty_column(df, col_name):
    return df[col_name].dropna().empty


def drop_empty_columns(df):
    empty_columns = [col for col in df.columns if is_empty_column(df, col)]
    df = df.drop(empty_columns, axis=1)
    return df
