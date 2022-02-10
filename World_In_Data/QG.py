import pandas as pd
import numpy as np







df = pd.read_csv("life-expectancy-years-vs-real-gdp-per-capita-2011us.csv")
af = df.loc[df['Life expectancy'].notnull()]
af = af.loc[af['GDP per capita'].notnull()]
af = af.loc[af['Code'].notnull()]
af = af.loc[af['Population (historical estimates)'].notnull()]
af = af.loc[af['Year'] == 2016]


#std mean for life ....
std_life_Expec = af['Life expectancy'].std()
mean_life_Expec = af['Life expectancy'].mean()
mean_std =   mean_life_Expec



# std mean for gdp
std_GDP = af['GDP per capita'].std()
mean_GDP = af['GDP per capita'].mean()
mean_std_GDP_low =  mean_GDP 
print(mean_GDP)

print('Standard Deviation of the life expectancy 2016:', mean_std_GDP_low)

new_df = af[af["Life expectancy"] < mean_std]

new_df = new_df[new_df["GDP per capita"] > mean_std_GDP_low]
print(new_df['GDP per capita'])


pd.set_option('display.max_rows', new_df.shape[0]+1)
print(new_df)
