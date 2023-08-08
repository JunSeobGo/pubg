from pandas import json_normalize
import requests
import pandas as pd
import numpy as np
import time

# champion info load
req2 = requests.get('http://ddragon.leagueoflegends.com/cdn/11.2.1/data/ko_KR/champion.json')

champ_ls = list(req2.json()['data'].keys())

champ_df = pd.DataFrame()
for i in range(len(champ_ls)):
    pre_df = json_normalize(req2.json()['data'][champ_ls[i]])
    champ_df = champ_df.append(pre_df)


champ_df.to_csv("champion.csv",header = False, index=False, encoding='utf-8')
