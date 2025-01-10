from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score


def scale_features(df):
    scaler = StandardScaler()
    return scaler.fit_transform(df.select_dtypes(np.number))


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
