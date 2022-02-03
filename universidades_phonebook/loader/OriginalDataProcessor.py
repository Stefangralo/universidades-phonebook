import pandas as pd

class OriginalDataProcessor():

    def __init__(self):
        self

    def load(self, resource):
        
        df = pd.read_excel(resource, header=[0,1])

        df['Departamento de Derecho Eclesiástico','Universidad'].fillna(method='ffill',axis=0,inplace=True)
        df['Departamento de Derecho Constitucional','Universidad'].fillna(method='ffill',axis=0,inplace=True)

        df = df.stack(level=0)
        df = df.reset_index(level=1)

        df.columns = ['Departamento', 'E-mail', 'Nombre', 'Teléfono', 'Universidad']

        df.dropna(how='all', subset=['E-mail', 'Nombre', 'Teléfono'],inplace=True)

        df.set_index('Nombre', inplace=True)

        print(df)
        return df

