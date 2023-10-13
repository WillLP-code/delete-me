import pandas as pd

def xy_sum(x, y):
    return x + y

def over_5(df):
    temp_df = df[df['Age'] >= 5]
    temp_df.reset_index(drop=True, inplace=True)
    return temp_df


