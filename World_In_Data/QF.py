import pandas as pd
import numpy as np
import matplotlib.pyplot as plt







df = pd.read_csv("life-expectancy-years-vs-real-gdp-per-capita-2011us.csv")
af = df.loc[df['Life expectancy'].notnull()]
af = af.loc[af['GDP per capita'].notnull()]
af = af.loc[af['Code'].notnull()]
af = af.loc[af['Population (historical estimates)'].notnull()]
af = af.loc[af['Year'] == 2016]

af['GDP'] = af['GDP per capita'] * af['Population (historical estimates)']

#std mean for life ....
std_life_Expec = af['Life expectancy'].std()
mean_life_Expec = af['Life expectancy'].mean()
mean_std =   mean_life_Expec



# std mean for gdp
std_GDP = af['GDP'].std()
mean_GDP = af['GDP'].mean()
mean_std_GDP_low =  mean_GDP 
print(mean_GDP)

print('Standard Deviation of the life expectancy 2016:', mean_std_GDP_low)

new_df = af[af["Life expectancy"] < mean_std]

new_df = new_df[new_df["GDP"] > mean_std_GDP_low]
print(new_df['GDP'])


pd.set_option('display.max_rows', new_df.shape[0]+1)
print(new_df)

# fig,ax = plt.subplots()
# ax.scatter(af.iloc[:,4],af.iloc[:,3])
# for i in range(len(af.iloc[:,0])):
#     ax.annotate(af.iloc[i,0],(af.iloc[i,4], af.iloc[i,3]),fontsize=6)

# plt.xlabel('GDP per capita [$]')
# plt.ylabel('Life expectancy [Years]')
# plt.title('Life expectancy for countries with high GDP per capita')
# fig.savefig("highGdpPerCapita_relatedLifeExp.pdf")
# plt.show()


