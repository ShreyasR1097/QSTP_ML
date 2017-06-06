import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
homicides=pd.read_csv("G:\Machine Learning\QSTP\QSTP17-PracticalML-master/database.csv",dtype = str)


plt.xlabel('Years',fontsize=20, fontweight='bold')
plt.ylabel('Total Count',fontsize=20, fontweight='bold')

a = homicides['Weapon'][homicides["Weapon"] == 'Knife'].groupby(homicides['Year']).value_counts().plot()    # Frequency of a weapon used vs year
homicides['Weapon'][homicides["Weapon"] == 'Shotgun'].groupby(homicides['Year']).value_counts().plot()
homicides['Weapon'][homicides["Weapon"] == 'Unknown'].groupby(homicides['Year']).value_counts().plot()
homicides['Weapon'][homicides["Weapon"] == 'Poison'].groupby(homicides['Year']).value_counts().plot()

patches, labels = a.get_legend_handles_labels()
my_labels = ['Knife','Shotgun','Unknown','Poison']
a.legend(patches,my_labels)


a1 = homicides['Relationship'][homicides["Relationship"] == 'Unknown'].groupby(homicides['Year']).value_counts().plot()   #Frequency of a relationship involved vs year
homicides['Relationship'][homicides["Relationship"] == 'Stranger'].groupby(homicides['Year']).value_counts().plot()    
homicides['Relationship'][homicides["Relationship"] == 'Son'].groupby(homicides['Year']).value_counts().plot()    
homicides['Relationship'][homicides["Relationship"] == 'Sister'].groupby(homicides['Year']).value_counts().plot()    

patches1, labels1 = a1.get_legend_handles_labels()
my_labels1 = ['Unknown','Stranger','Son','Sister']
a1.legend(patches1,my_labels1)


homicides['Weapon'].value_counts().plot.box()   #Box plot of weapon Vs year