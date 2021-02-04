import glob
import pandas as pd


def get_csv_data():
    filenames = glob.glob('I:/Fiverr Projects/oil_gasEnv/og_analysis/data/Oil and Gas Production data' + "/*.csv")
    dfs = []
    for filename in filenames:
        dfs.append(pd.read_csv(filename))

    df1 = pd.concat(dfs, ignore_index=True)
    # print(df1.columns)
    df = df1
    return df
# data = df.groupby('County')
# print(data.head())
