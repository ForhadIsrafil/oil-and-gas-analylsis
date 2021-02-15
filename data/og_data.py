import glob
import pandas as pd
import os
columns_array = ['API_WellNo', 'County', 'CoName', 'Hole', 'SideTrck', 'Completion', 'Well_Typ', 'Field',
                 'Wl_Status',
                 'Well_Nm', 'town', 'Prod', 'Form', 'MonthProd', 'GasProd', 'WaterProd', 'OilProd', 'Year',
                 ]

root_dir = os.path.abspath(os.curdir)
def get_csv_data():
    filenames = glob.glob(str(root_dir).replace('\\','/') + "/data/Oil and Gas Production data/*.csv")
    dfs = []
    for filename in filenames:
        dfs.append(pd.read_csv(filename))

    df1 = pd.concat(dfs, ignore_index=True)

    d = df1.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]

    # print(df1.columns)
    # df1.columns = df1.columns.str.strip()
    return d
# data = df.groupby('County')
# print(data.head())
# get_csv_data()
