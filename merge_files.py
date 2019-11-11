# -*-coding:utf-8-*-
import pandas as pd

for i in range(1, 86):
    count = 0
    dataset = pd.read_csv("./CSV_1/"+str(i)+".csv", header=None)
    ls = [num for num in range(0, len(dataset), 3)]
    dataset = dataset.transpose()[ls].transpose()    # 隔3帧提取一次    可考虑换eval函数
    print len(dataset)
    a = len(dataset)
    for n in range(a, 150):  # 插入一行
        dataset.loc[n * 3] = dataset.loc[a * 3 - 3]     # 运算速度还不够快
    dataset.to_csv("./one_file3.csv", mode='a', sep=',', index=False, header=False)

for i in range(101, 186):
    count = 0
    dataset = pd.read_csv("./CSV_1/"+str(i)+".csv", header=None)
    ls = [num for num in range(0, len(dataset), 3)]
    dataset = dataset.transpose()[ls].transpose()    # 隔3帧提取一次    可考虑换eval函数
    print len(dataset)
    a = len(dataset)
    for n in range(a, 150):  # 插入一行
        dataset.loc[n * 3] = dataset.loc[a * 3 - 3]     # 运算速度还不够快
    dataset.to_csv("./one_file3.csv", mode='a', sep=',', index=False, header=False)
