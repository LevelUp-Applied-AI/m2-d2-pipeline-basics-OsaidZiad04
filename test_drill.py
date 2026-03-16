"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # TODO: Create a pd.Series with at least one NaN value
    series = pd.Series([1, 2, np.nan, 4, 5])
    # TODO: Call clean_column() on it
    cleaned_series = clean_column(series)
    # TODO: Assert no NaN values remain in the result
    assert cleaned_series.isnull().sum() == 0
    # TODO: Assert the NaN was filled with the correct median value
    assert cleaned_series.iloc[2] == 3.0


def test_compute_revenue():
    # TODO: Create two small pd.Series (quantity and price)
    quantity = pd.Series([1, 2, 3])
    price = pd.Series([10, 20, 30])
    # TODO: Call compute_revenue() on them
    revenue = compute_revenue(quantity, price)
    # TODO: Assert the result matches the expected element-wise product
    assert revenue.equals(pd.Series([10, 40, 90]))