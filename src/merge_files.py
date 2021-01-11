# -*-coding:utf-8-*-
import pandas as pd
import feature as fe

for j in [2, 3, 4, 5, 6]:
    for i in range(1, 101):
        count = 0
        dataset = pd.read_csv("/home/pdzhu/GestureRecognitionSourceFiles/data/"+str(j)+"/"+str(i)+".csv", header=None)
        ls = [num for num in range(0, len(dataset), 3)]
        dataset = dataset.loc[ls]  # 隔3帧提取一次    可考虑换eval函数

        data = pd.DataFrame()
        fe.feature_s(dataset, data)
        fe.feature_d(dataset, data)
        fe.feature_v(dataset, data)
        fe.feature_p(dataset, data)
        fe.feature_l(dataset, data)

        data = ((data-data.mean())/data.std()).fillna(0)

        fe.feature_res(dataset, data)

        print len(data)
        a = len(data)

        if a < 150:
            for n in range(a, 150):  # 插入一行
                data.loc[n * 3] = data.loc[a * 3 - 3]     # 运算速度还不够快
            data.to_csv("/home/pdzhu/GestureRecognitionSourceFiles/temp/109.csv",
                        mode='a', sep=',', index=False, header=False)
