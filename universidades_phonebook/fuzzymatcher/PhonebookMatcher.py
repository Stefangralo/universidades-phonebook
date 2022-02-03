import pandas as pd
import difflib as diff

class PhoneBookMatcher():

    def __init__(self):
        self

    def fuzzyMerge(self, oldDf, newDf):
        newDf.index = newDf.index.map(lambda x: diff.get_close_matches(x, str(oldDf.index).upper))
        
        mergedDf = oldDf.join(newDf)

        print(mergedDf)