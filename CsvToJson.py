import pandas as pd
df = pd.read_csv('466920-2023-03.csv')
df = df.drop(columns=['ObsTime','SeaPres','Td_dew_point','WS','WD','WSGust','WDGust','WGustTime','PrecpMax10','PrecpMax10Time','PrecpMax60','PrecpMax60Time','GloblRad','EvapA','Cloud_Amount'])
df
df.to_json('temp.json')