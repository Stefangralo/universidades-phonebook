import pandas as pd

class ScrapedDataProcessor():

    def __init__(self):
        self

    def load(self, resource):

        df = pd.read_json(resource)

        print(df.columns)
        df.set_index('name', inplace=True)

        print(df)

        return df