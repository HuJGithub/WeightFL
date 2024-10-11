import numpy as np
import pandas as pd
import random
from data_process.ProcessedData import ProcessedData


class SFITF(ProcessedData):

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.rest_columns = raw_data.rest_columns


    def process(self):
        DF = 1/self.feature_df.sum(axis=0)
        print(DF)

        M = len(self.feature_df)
        print(N)

        ITF = np.log(M/self.feature_df.sum(axis=1))
        print(SFITF)

        SFITF=DF*ITF
       
        for col in self.feature_df.columns:
            self.feature_df[col] *= SFITF[col]

        
        print(self.feature_df)
        self.data_df = pd.concat([self.feature_df, self.label_df], axis=1)
        #print(self.data_df)
