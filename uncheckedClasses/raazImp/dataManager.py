import pandas as pd
import ta
import os.path
from os import path


class DataFile:
    def __init__(self, fileName):
        self.fileName = fileName
        if (path.exists(fileName) != True):
            print("ERROR: File \"" + fileName + "\" does not exist in current directory.")
            self = none
            return none
        df = pd.read_csv(fileName, sep=',')
        #df = ta.utils.dropna(df)
        df = ta.add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True) 


    #def loadData(self):

