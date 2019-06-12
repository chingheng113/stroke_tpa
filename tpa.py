import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import Imputer
import os
current_path = os.path.dirname(__file__)


def is_tpa():
    df_case = pd.read_csv(os.path.join(current_path, 'data', 'raw', 'CASEDCASE.csv'))
    df_tpa = df_case[['IVTPATH_ID', 'IVTPA_DT', 'IVTPAH_NM', 'IVTPAM_NM', 'IVTPAMG_NM', 'NIVTPA_ID']]
    df_tpa.loc[~df_tpa.IVTPATH_ID.isin(['1', '2'])] = np.nan
    df_tpa['IVTPA_DT'] = pd.to_datetime(df_tpa['IVTPA_DT'], format='%Y-%M-%d', errors='ignore')
    df_tpa['NIVTPA_ID'] = [np.nan if np.isnan(x) else -1 for x in df_tpa['IVTPATH_ID']]
    df_case['is_tpa'] = [1 if x == -1 else 0 for x in df_tpa['NIVTPA_ID']]
    df_tpa = df_case[df_case.is_tpa == 1]
    return df_case


if __name__ == '__main__':
    is_tpa()