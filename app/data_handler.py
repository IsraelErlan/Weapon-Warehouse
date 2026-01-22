import pandas as pd 
import numpy as np
import json

def csv_to_df(csv):
    df = pd.read_csv(csv)
    return df


def categorization_by_range_of_injury(df):
    df['risk_level'] = pd.cut(df['range_km'], 
                                bins=[0, 20, 100, 300, np.inf],
                                labels=['low', 'medium', 'high', 'extreme'])

def handling_missing_values(df):
    df['manufacturer'] = df['manufacturer'].fillna("Unknown")


def df_to_json(df):
    data = df.to_json()
    data = json.loads(data)
    print(type(data))
    return data


