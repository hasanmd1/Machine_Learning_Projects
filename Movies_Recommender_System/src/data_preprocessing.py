import pandas as pd
import numpy as np


def clean_data(dataframe, column_names):
    """
    Fill NaN values in specified columns of the dataframe with the mean of the respective columns.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataframe to be cleaned.
    column_names : list of str
        The names of the columns to be cleaned. If None or empty, the dataframe is returned as is.

    Returns
    -------
    pandas.DataFrame
        The dataframe with NaN values in specified columns replaced with the mean of the respective columns.
    """
    if column_names is None or len(column_names) == 0:
        return pd.DataFrame(dataframe)
    for column_name in column_names:
        dataframe[column_name] = dataframe[column_name].fillna(dataframe[column_name].mean())
    return pd.DataFrame(dataframe)


def clean_data_empty_string(dataframe, column_names):

    """
    Replace empty strings in dataframe columns with NaNs.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataframe to be cleaned.
    column_names : list
        The names of columns to be cleaned.

    Returns
    -------
    pandas.DataFrame
        The cleaned dataframe.
    """
    if column_names is None or len(column_names) == 0:
        return pd.DataFrame(dataframe)
    for column_name in column_names:
        print(column_name)
        dataframe[column_name] = dataframe[column_name].fillna('Unknown')
    return pd.DataFrame(dataframe)
