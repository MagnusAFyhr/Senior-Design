import pandas as pd
import os.path
from os import path
from ta_lib_init import TALIBINIT

class DataFile:
    def __init__(self, fileName):
        self.fileName = fileName
        if (path.exists(fileName) != True):
            print("ERROR: File \"" + fileName + "\" does not exist in current directory.")
            self = none
            return none
        df = pd.read_csv(fileName, sep=',')
        df = TALIBINIT(df)
        df.to_csv("bigchicken.csv", sep=',')

    #def loadData(self):

