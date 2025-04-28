import pandas as pd

def preprocess(df, region_df):
    # Keep only Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Merge with region data
    df = df.merge(region_df, on='NOC', how='left')

    # Handle possible duplicate columns after merge
    df = df.loc[:, ~df.columns.duplicated()]

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    #one hot encoding  medals
    df = pd.concat([df, pd.get_dummies(df['Medal'],)], axis=1)

    return df
