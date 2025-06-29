from etl.transform import is_empty_column
import numpy as np
import pandas as pd
import pytest


@pytest.mark.parametrize(
    "column_data, expected",
    [
        ([np.nan, np.nan, np.nan], True),
        ([1, 2, 3], False),
        ([1, np.nan, 3], False),
        ([None, np.nan, None], True),
        ([2, None, 3], False),
    ],
)
def test_is_empty_column(column_data, expected):
    df = pd.DataFrame({"col": column_data})
    assert is_empty_column(df, "col") == expected
