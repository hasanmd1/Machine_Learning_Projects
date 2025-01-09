import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_data(location):
    return pd.read_csv(location, sep=',')


def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


# if __name__ == '__main__':
#     df = load_data('../dataset/raw/creditcard.csv')
#     over_sampling(df)
