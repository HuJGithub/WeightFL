import numpy as np
import pandas as pd
import random
from data_process.ProcessedData import ProcessedData


class IDF(ProcessedData):

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.rest_columns = raw_data.rest_columns


    def process(self):
        DF = self.feature_df.sum(axis=0)
        print(DF)

        # 计算文档总数
        N = len(self.feature_df)
        print(N)

        # 计算每列的IDF
        IDF = np.log(N / (DF))/DF**0.5
        print(IDF)
        # 遍历整个DataFrame，将每个元素乘以对应的IDF值
        for col in self.feature_df.columns:
            self.feature_df[col] *= IDF[col]

        # 打印修改后的DataFrame
        print(self.feature_df)
        self.data_df = pd.concat([self.feature_df, self.label_df], axis=1)
        #print(self.data_df)
