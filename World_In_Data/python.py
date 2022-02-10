import numpy as np
import matplotlib.pyplot as plt
import matplotlib as style
import pandas as pd
import numpy.polynomial.polynomial as poly



df = pd.read_csv("life-expectancy-years-vs-real-gdp-per-capita-2011us.csv")

# af = df.loc[df['Entity'] == "World"]
# af = af.loc[af['Life expectancy'].notnull()]
# af = af.loc[af['GDP per capita'].notnull()]

af = df.loc[df['Life expectancy'].notnull()]
af = af.loc[af['GDP per capita'].notnull()]
af = af.loc[af['Year'] == 2016]
af['log GDP'] = np.log10(af['GDP per capita'])
af['log life'] = np.log2(af['Life expectancy'])

# Report_Card.loc[:,"Grades"]


print(af)
print(af.loc[:,"GDP per capita"])
print(af.loc[:,"Life expectancy"])





plt.scatter(af.loc[:,"GDP per capita"], af.loc[:,"Life expectancy"])
plt.title("Life expectancy vs GDP per capita")
plt.xlabel("GDP per capita [$]")
plt.ylabel("Life expectancy [Years]")

plt.show()



