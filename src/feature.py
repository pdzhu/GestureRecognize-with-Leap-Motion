# -*-coding:utf-8-*-
import pandas as pd
import numpy as np


# 手握球相对大小 S
def feature_s(ds, da):
    col = da.shape[1]

    da[col] = (ds.loc[:, 27] / ds.loc[:, 26]).fillna(0)
    da[col + 1] = (ds.loc[:, 56] / ds.loc[:, 55]).fillna(0)


# 指尖掌心 D
def feature_d(ds, da):
    col = da.shape[1]

    # 左手
    for i in range(5):
        da[col + i] = (
                (ds.loc[:, 11 + i * 3] - ds.loc[:, 5]).apply(np.square) +
                (ds.loc[:, 12 + i * 3] - ds.loc[:, 6]).apply(np.square) +
                (ds.loc[:, 13 + i * 3] - ds.loc[:, 7]).apply(np.square)
                ).apply(np.sqrt)

    # 右手
    for j in range(5):
        da[col + 5 + j] = (
                (ds.loc[:, 40 + j * 3] - ds.loc[:, 34]).apply(np.square) +
                (ds.loc[:, 41 + j * 3] - ds.loc[:, 35]).apply(np.square) +
                (ds.loc[:, 42 + j * 3] - ds.loc[:, 36]).apply(np.square)
        ).apply(np.sqrt)


# 掌心相对速度
def feature_v(ds, da):
    col = da.shape[1]

    # 左手
    da[col] = (ds.loc[:, 9].apply(np.square) +
               ds.loc[:, 10].apply(np.square)
               ).apply(np.sqrt) * (ds.loc[:, 3] / 180)

    da[col + 1] = (ds.loc[:, 8].apply(np.square) +
                   ds.loc[:, 10].apply(np.square)
                   ).apply(np.sqrt) * (ds.loc[:, 2] / 180)

    da[col + 2] = (ds.loc[:, 8].apply(np.square) +
                   ds.loc[:, 9].apply(np.square)
                   ).apply(np.sqrt) * (ds.loc[:, 4] / 180)

    # 右手
    da[col + 3] = (ds.loc[:, 38].apply(np.square) +
                   ds.loc[:, 39].apply(np.square)
                   ).apply(np.sqrt) * (ds.loc[:, 32] / 180)

    da[col + 4] = (ds.loc[:, 37].apply(np.square) +
                   ds.loc[:, 39].apply(np.square)
                   ).apply(np.sqrt) * (ds.loc[:, 31] / 180)

    da[col + 5] = (ds.loc[:, 37].apply(np.square) +
                   ds.loc[:, 38].apply(np.square)
                   ).apply(np.sqrt) * (ds.loc[:, 33] / 180)


# 手掌相对位置P
def feature_p(ds, da):
    col = da.shape[1]

    # 左手
    for i in range(3):
        da[col + i] = ds.loc[:, 5 + i] - ds.loc[:, 28 + i]

    # 右手
    for j in range(3):
        da[col + 3 + j] = ds.loc[:, 34 + j] - ds.loc[:, 57 + j]


# 指尖间距 L
def feature_l(ds, da):
    col = da.shape[1]

    # 左手
    for i_x in range(5):   # 0 1 2 3 4
        for i_y in range(i_x + 1, 5):
            da[col] = (
                    (ds.loc[:, 11 + i_x * 3] - ds.loc[:, 11 + i_y * 3]).apply(np.square) +
                    (ds.loc[:, 12 + i_x * 3] - ds.loc[:, 12 + i_y * 3]).apply(np.square) +
                    (ds.loc[:, 13 + i_x * 3] - ds.loc[:, 13 + i_y * 3]).apply(np.square)
            ).apply(np.sqrt)
            col += 1

    # 右手
    for j_x in range(5):   # 0 1 2 3 4
        for j_y in range(j_x + 1, 5):
            da[col] = (
                    (ds.loc[:, 40 + j_x * 3] - ds.loc[:, 40 + j_y * 3]).apply(np.square) +
                    (ds.loc[:, 41 + j_x * 3] - ds.loc[:, 41 + j_y * 3]).apply(np.square) +
                    (ds.loc[:, 42 + j_x * 3] - ds.loc[:, 42 + j_y * 3]).apply(np.square)
            ).apply(np.sqrt)
            col += 1


if __name__ == "__main__":
    dataset = pd.read_csv("/home/pdzhu/GestureRecognitionSourceFiles/temp/2.csv", header=None)

    data = pd.DataFrame()
    feature_p(dataset, data)
    feature_l(dataset, data)

    data.to_csv("3.csv", sep=',', index=False, header=False)
