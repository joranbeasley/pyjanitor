from janitor.testing_utils.fixtures import dataframe
import pandas as pd
import numpy as np


def test_transform_column(dataframe):
    # replacing the data of the original column

    df = dataframe.transform_column("a", np.log10)
    expected = pd.Series(np.log10([1, 2, 3] * 3))
    expected.name = "a"
    pd.testing.assert_series_equal(df["a"], expected)


def test_transform_column_with_dest(dataframe):
    # creating a new destination column

    expected_df = dataframe.assign(a_log10=np.log10(dataframe["a"]))

    df = dataframe.copy().transform_column(
        "a", np.log10, dest_col_name="a_log10"
    )

    pd.testing.assert_frame_equal(df, expected_df)
