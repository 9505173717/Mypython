#!/usr/bin/env python
# coding: utf-8

# In[82]:

import re
import os
import numpy as np
import pandas as pd

df=pd.read_csv(r"D:\Nag\python\nyc_parking_tickets_extract.csv",sep=',')

df['Issue Date']=pd.to_datetime(df['Issue Date'])

mask = (df['Issue Date'] >= '7/13/2016') & (df['Vehicle Make'].str.match("BMW"))
df_1=df.loc[mask]
print(df_1)
print("Nag")




