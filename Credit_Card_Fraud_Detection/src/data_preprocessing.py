import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


def load_data(location):
    return pd.read_csv(location, sep=',')


def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def scale_features(df):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.select_dtypes(np.number))
    return pd.DataFrame(scaled_features, columns=df.select_dtypes(np.number).columns)


def under_sampling(df):
    df = df.sample(frac=1, random_state=42)
    df_0 = df[df['Class'] == 0]
    df_1 = df[df['Class'] == 1]
    df_1_under = df_1.sample(len(df_0), random_state=42)
    new_df = pd.concat([df_0, df_1_under], axis=0)

    # basically shuffling data, fixing indexing and returning dataframe
    return new_df.sample(frac=1, random_state=42).reset_index(drop=True)


def over_sampling(df):
    df_0 = df[df['Class'] == 0]
    df_1 = df[df['Class'] == 1]
    df_0_over = df_0.sample(len(df_1), replace=True)
    df = pd.concat([df_1, df_0_over], axis=0)
    return df
