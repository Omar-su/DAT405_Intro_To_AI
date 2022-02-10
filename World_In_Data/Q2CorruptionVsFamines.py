import numpy as np
import matplotlib.pyplot as plt
import matplotlib as style
import pandas as pd
import numpy.polynomial.polynomial as poly


# Reading the datasets
cf = pd.read_csv("TI-corruption-perception-index.csv")
ff = pd.read_csv("food-supply-kcal.csv")

# Cleaning data of the corruption dataset
cf = cf.loc[cf['Corruption Perception Index - Transparency International (2018)'].notnull()]
cf = cf.loc[cf['Entity'] != 'World']
cf = cf.loc[cf['Code'].notnull()]
cf = cf.loc[cf['Year'] == 2016]



# Cleaning data of the food supply dataset
ff = ff.loc[ff['Food supply (kcal/capita/day) (FAO, 2020)'].notnull()]
ff = ff.loc[ff['Entity'] != 'World']
ff = ff.loc[ff['Code'].notnull()]
ff = ff.loc[ff['Year'] == 2016]


# Merging the two datasets
cff = pd.merge(cf,ff)




#std mean for Corruption Perception Index
mean_corruption = cff['Corruption Perception Index - Transparency International (2018)'].mean()

print(mean_corruption)

# std and mean computation for Food supply
mean_kcal = cff['Food supply (kcal/capita/day) (FAO, 2020)'].mean()
print(mean_kcal)


print('Standard Deviation of the life expectancy 2016:', mean_kcal)

#We only select countries with a Corruption Perception Index below the mean and a Food supply above the mean
new_df = cff[cff["Corruption Perception Index - Transparency International (2018)"] > mean_corruption]

new_df = new_df[new_df["Food supply (kcal/capita/day) (FAO, 2020)"] < mean_kcal]
print(new_df)


# Plotting the comparison of the datasets
plt.scatter(cff.loc[:,"Food supply (kcal/capita/day) (FAO, 2020)"],cff.loc[:,"Corruption Perception Index - Transparency International (2018)"])
plt.title("Corruption Perception Index vs Food supply")
plt.xlabel("Food supply [kcal]")
plt.ylabel("Corruption Perception Index [Low values = high corruption]")

plt.show()

