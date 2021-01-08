# coding=utf-8
import numpy as np
import pandas as pd
from keras.models import load_model
import tensorflow as tf
import os
import time
import sys

sys.path.insert(0, "../lib")
sys.path.insert(0, "../lib/x64")

# Load the model
model = load_model('model_test9_8pip.h5')
print "Model Loaded"
graph = tf.get_default_graph()


# def main(i):
#     data = pd.read_csv('/home/pdzhu/GestureRecognitionSourceFiles/CSV_1/' + str(i) + '.csv', header=None)
#     df_right = pd.DataFrame(data=data)
#     df_right = df_right.transpose()
#     ls = [num for num in range(0, len(df_right), 3)]
#     df_right = df_right.transpose()[ls].transpose()    # 隔3帧提取一次    可考虑换eval函数
#     print i
#     a = len(df_right)
#     for n in range(a, 150):  # 插入一行
#         df_right.loc[n * 3] = df_right.loc[a * 3 - 3]     # 运算速度还不够快
#
#     x = df_right.iloc[:, 1:49].values
#     with graph.as_default():
#         y_pred = model.predict(np.reshape(x, (1, x.shape[0], x.shape[1])))
#     pred = np.argmax(y_pred)
#     # Eliminate the False Postives
#     print y_pred
#     print pred
#     m = 0 if 85 < i < 101 else 1
#     # if (y_pred[0][0] or y_pred[0][1]) >= 0.2:
#     if y_pred[0][0] >= 0.5 or y_pred[0][1] >= 0.5:
#         if pred == m:
#             count = count + 1


# if __name__ == "__main__":
lsa = [_ for _ in range(86, 101)] + [_ for _ in range(186, 201)]
count = 0
for i in lsa:
    data = pd.read_csv('/home/pdzhu/GestureRecognitionSourceFiles/CSV_1/' + str(i) + '.csv', header=None)
    df_right = pd.DataFrame(data=data)
    df_right = df_right.transpose()
    ls = [num for num in range(0, len(df_right), 3)]
    df_right = df_right.transpose()[ls].transpose()  # 隔3帧提取一次    可考虑换eval函数
    print i
    a = len(df_right)
    for n in range(a, 150):  # 插入一行
        df_right.loc[n * 3] = df_right.loc[a * 3 - 3]  # 运算速度还不够快

    x = df_right.iloc[:, 1:49].values
    with graph.as_default():
        y_pred = model.predict(np.reshape(x, (1, x.shape[0], x.shape[1])))
    pred = np.argmax(y_pred)
    # Eliminate the False Postives
    print y_pred
    print pred
    m = 0 if 85 < i < 101 else 1
    print m
    # if (y_pred[0][0] or y_pred[0][1]) >= 0.2:
    if y_pred[0][0] >= 0.4 or y_pred[0][1] >= 0.4:
        if pred == m:
            count = count + 1
print count
