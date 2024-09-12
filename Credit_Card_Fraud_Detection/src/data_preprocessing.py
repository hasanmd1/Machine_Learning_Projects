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
    return scaler.fit_transform(df.select_dtypes(np.number))


# return pd.DataFrame(scaled_features, columns=df.select_dtypes(np.number).columns)


def under_sampling(df, target):
    df = df.sample(frac=1, random_state=42)
    df_0 = df[df[target] == 0]
    df_1 = df[df[target] == 1]
    df_0_under = df_0.sample(n=len(df_1), random_state=42)
    new_df = pd.concat([df_1, df_0_under], axis=0)

    # basically shuffling data, fixing indexing and returning dataframe
    return new_df.sample(frac=1, random_state=42).reset_index(drop=True)


def over_sampling(df, target_name):
    # first separate features and target
    features = df.drop(columns=target_name, axis=1)
    target = df[target_name]

    # apply SMOTE
    smote = SMOTE(random_state=42, k_neighbors=10)
    # fit for all fraud non-fraud number and apply the transform
    features_resampled, target_resampled = smote.fit_resample(features, target)

    features_resampled_df = pd.DataFrame(features_resampled, columns=features.columns)
    target_resampled_df = pd.DataFrame(target_resampled, columns=[target_name])

    # recombine features and target and return
    return pd.concat([features_resampled_df, target_resampled_df], axis=1)

# if __name__ == '__main__':
#     df = load_data('../dataset/raw/creditcard.csv')
#     over_sampling(df)
