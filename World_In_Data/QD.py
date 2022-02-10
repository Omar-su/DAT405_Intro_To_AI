import numpy as np
import matplotlib.pyplot as plt
import matplotlib as style
import pandas as pd
import numpy.polynomial.polynomial as poly



df = pd.read_csv("life-expectancy-years-vs-real-gdp-per-capita-2011us.csv")
af = df.loc[df['Life expectancy'].notnull()]
af = af.loc[af['GDP per capita'].notnull()]
af = af.loc[af['Entity'] != 'World']
af = af.loc[af['Code'].notnull()]
af = af.loc[af['Year'] == 2016]


std_life_Expec = af['Life expectancy'].std()
mean_life_Expec = af['Life expectancy'].mean()
mean_std = std_life_Expec + mean_life_Expec

print('Standard Deviation of the life expectancy 2016:', mean_std)


new_df = af[af["Life expectancy"] > mean_std]



pd.set_option('display.max_rows', new_df.shape[0]+1)
print(new_df)



