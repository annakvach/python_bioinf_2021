# https://www.kaggle.com/c/titanic/data?select=test.csv
# i download train.csv

# install packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pd.set_option('display.max_columns', None) # to see all cols


# read data and put it in DataFrame

path_to_data = "train_titanic.csv"

'''path_to_data = input("Input path to data: ")
if path_to_data == "":
    path_to_data = "train_titanic.csv"
    print("Default: train_titanic.csv")'''

df = pd.read_csv(path_to_data)

# introduction to data
print("\n\n INTRODUCTION TO DATA\n\n\n")
print("----------First 10 rows of dataframe---------- \n", df.head(10))
print()

print("----------Data dictionary + which data are NA? ---------- \n")

words = df.columns.values
na_data_for_cols = df.isna().sum()
description = ["Id in dataset",
               "0 - died, 1 - survived",
               "Class od the ticket (1st - Upper Class, 2nd - Middle Class, 3rd - Lower Class)",
               "Name", "Sex", "Age",
               "Number of siblings or partners",
               "Number of children / parents",
               "ticket number",
               "Money paid for travel",
               "Number of the room (cabin)",
               "Port of embrakation (place where the travel start or end)"]

temp_df = pd.DataFrame({"NA": na_data_for_cols, "description": description})
print(temp_df)
n_observations = df.shape[0]
print("\n\n")
print("We have", n_observations, "observations. From them", df.shape[0] - df.dropna().shape[0], "are with NA.")
print("We cant delete so much observations, so we will create second dataset \n",
      "with removed 1 col (Cabin) and rows (have Na in Embarked or in Age col)\n"
      "with cabin data we will work latter")

# For which people we don`t know age?
print("\n")
print("----------For which people we don`t know age?---------- ")
df_3 = df.Age.isnull().groupby(df['Pclass']).sum().astype(int).reset_index(name='Age_NA')
print(df_3)
# sns.barplot(x=["Upper Class", "Middle Class", "Lower Class"], y="Age_NA", data=df_3)
# plt.show()
print("For some reason we don`t know age mostly for people from 3d class based on this dataset.")
print("I did not find the exact reason for this, but it can be assumed that people from lower social strata may not know their exact age.")
print("We deleted cases with no age data.")

# remove col (Cabin)
print("\n\n")
print("----------First 10 rows of dataframe with no NA---------- \n", df.head(10))
df_2 = df.drop(labels=["Cabin"], axis=1)
# remove rows with Na
df_2 = df_2. dropna()
pd.set_option('display.max_columns', None) # to see all cols
print(df_2.head(10))
# sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='cividis')
# plt.show()
# sns.heatmap(df_2.isnull(), yticklabels=False, cbar=False, cmap='cividis')
# plt.show()
# correlation
print("\n\n")


print("----------Description of df---------- ")
print(df_2.describe())
print(df_2.describe(include='O'))
print("\n\n")

# Pair plot for breef overview
# sns.pairplot(df_2.drop(['PassengerId'], axis=1), hue="Sex", palette="bwr", height=1.2)
# plt.show()
print("From pairplot we can that: \n"
      " - there were more men than women on the ship \n"
      " - more men died than were saved\n"
      " - more women were saved than died \n"
      " - there were approximately equal numbers of women in different classes, but men were most often in the Lower Class \n"
      " - Children (boys and girls) were approximately equally divided, and among adults there were more men\n"
      "...")

print("\n\nWe will check:\n"
      "Which class of women survived the most?\n"
      "Men from which class have survived to the greatest extent?\n"
      "How did age and gender affect ability to survive?\n"
      "Did the living room affect ability to survive?\n\n")

# factor plot Sex vs Survived
print("\n\n")

sns.catplot(data=df_2, x='Survived', col='Sex', kind='count', palette="PiYG")
plt.show()

# factor plot Pclass vs Survived
print("\n\n")
# sns.catplot(data=df_2, x='Survived', col='Pclass', kind='count', palette="PiYG")
# plt.show()

