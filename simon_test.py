import pandas as pd
pd.options.mode.chained_assignment = None

df = pd.DataFrame([{'jan':1,
                    'feb':1,
                    'mar':1,
                    'apr':1,
                    'may':1},
                    {'jan':0,
                    'feb':1,
                    'mar':1,
                    'apr':1,
                    'may':1},
                    {'jan':0,
                    'feb':0,
                    'mar':1,
                    'apr':1,
                    'may':1},
                    {'jan':0,
                    'feb':0,
                    'mar':0,
                    'apr':1,
                    'may':1},
                    {'jan':0,
                    'feb':0,
                    'mar':0,
                    'apr':0,
                    'may':1},
                    {'jan':0,
                    'feb':1,
                    'mar':1,
                    'apr':1,
                    'may':0},
                    ])


df.iloc[:,0] = df.iloc[:,0].apply(lambda x: 'existing' if x == 1 else 'none')


months = df.columns
df.reset_index(inplace=True)

def f(df, col_1, col_2):

    existing_df = df[((df[col_1] == 'existing') |(df[col_1] == 'new')) & (df[col_2] == 1)]
    existing_df[col_2] = 'existing'
    left_df =  df[(df[col_1] == 'existing') & (df[col_2] == 0)]
    left_df[col_2] = 'left'
    new_df = df[(df[col_1] == 'none') & (df[col_2] == 1)]
    new_df[col_2] = 'new'
    temp_df = pd.concat([existing_df, left_df, new_df]).sort_index()
    index_list = temp_df['index'].tolist()
    none_df = df[~df['index'].isin(index_list)]
    none_df[col_2] = 'none'
    df = pd.concat([temp_df, none_df]).sort_index()
    return df[col_2]

# df[2] = f(df, 1, 2)
# df[3] = f(df, 2, 3)
# df[4] = f(df, 3, 4)
# df[5] = f(df, 4, 5)

for i in range(len(months)):
    if i > 0:
        df[months[i]] = f(df, months[i-1], months[i])

print(df)