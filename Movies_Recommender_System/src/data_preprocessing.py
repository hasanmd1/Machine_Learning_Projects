import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class CleanData:
    def __init__(self):
        pass

    def clean_data(self, dataframe, column_name):
        if column_name is None:
            return dataframe
        dataframe: pd.DataFrame = dataframe[column_name].fillna(0)
        return dataframe

    def clean_data_empty_string(self, dataframe, column_name):
        if column_name is None:
            return dataframe
        dataframe: pd.DataFrame = dataframe[column_name].fillna('Unknown')
        return dataframe
