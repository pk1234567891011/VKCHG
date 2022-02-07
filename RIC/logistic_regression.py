import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import math
titanic_data=pd.read_csv("titanic.csv")
print(titanic_data)
sns.countplot('Survived', hue="Sex" ,data=titanic_data)
plt.show()
titanic_data["Age"].plot.hist()
plt.show()
titanic_data.info()
titanic_data.isnull().sum()
sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap="viridis")
plt.show()
sns.boxplot(x="Pclass",y="Age",data=titanic_data)
plt.show()
pd.get_dummies(titanic_data['Sex'])

