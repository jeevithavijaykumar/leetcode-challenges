""" 2883. Drop Missing Data """
""" Given students dataframe, There are some rows having missing values in the name column.
Write a solution to remove the rows with missing values."""

import pandas as pd

def dropMissingData(students):
    return(students.dropna(subset=['name'],inplace=True))