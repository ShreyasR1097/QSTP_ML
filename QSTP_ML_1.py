import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


homicides=pd.read_csv("G:\Machine Learning\QSTP\QSTP17-PracticalML-master/database.csv",dtype = str)

print(homicides["Crime Solved"][homicides["Crime Solved"] == 'Yes'].value_counts()) #How many crimes were solved

print(homicides["Weapon"].value_counts().nlargest(5))  #Top 5 weapons used

s = homicides['Weapon'].groupby(homicides['City']).value_counts(normalize = True)
print(s.groupby(level=0).nlargest(1))    #Top weapon in each state with its percentage(count of weapon/total count)

plt.xlabel('Years',fontsize=20, fontweight='bold')
plt.ylabel('Total Count',fontsize=20, fontweight='bold')
homicides['Year'].value_counts().plot(kind = 'bar')    #Bar plot of number of homicide vs year

