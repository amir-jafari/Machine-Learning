# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Pandas Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import pandas as pd
import numpy as np
# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------

titanic = pd.read_csv('titanic_train.csv')

print(type(titanic))
print(len(titanic))
nrows, ncols = titanic.shape

print(nrows)
print(ncols)

print(titanic.head())
print(titanic.head(3) )

random_rows = titanic.sample(n=10)
print(random_rows)

random_5_percent = titanic.sample(frac=.05)
print(random_5_percent)

col = titanic.columns
print(col)

info = titanic.info()
print(info)


del titanic['Cabin']
titanic.head()
titanic.describe()

index2 = titanic.index
print(index2)

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- More Data Wrangling----------------------------------------
Null = titanic['PassengerId'].isnull()
sum(Null)

unique = titanic['PassengerId'].nunique()
print(unique)



titanic.set_index('PassengerId', inplace=True)
print(titanic.index)

survived = titanic['Survived'].unique()
print(survived)


print(titanic['Pclass'].unique())
print(titanic['Pclass'].nunique())

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Sorting ---------------------------------------------------

titanic.sort_values(by=['Sex', 'Age'])
titanic.sort_values(by=['Sex', 'Age'], ascending=[False, True])
titanic.sort_values(by=['Sex', 'Age'], ascending=[False, True], inplace=True)
titanic.head()

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Filtering ---------------------------------------------------

age_is_missing = titanic['Age'].isnull()
print(sum(age_is_missing))
print(sum(~age_is_missing))

p22 = titanic.loc[age_is_missing, :]
print(p22)
p23 = titanic.loc[~age_is_missing, :]
print(p23)

titanic.loc[titanic['Age'].isnull()]
titanic.loc[~titanic['Age'].isnull()]



less_18 = titanic.query('Age < 18')
print(less_18)


between = titanic.query('Age < 18 and Sex=="female"')
print(between)

p24 = titanic.query('Age < 18 and Sex=="female" and Survived==1').shape[0]
print(p24)

p25 = titanic.query('Age < 18 and Sex=="female" and Survived==0').shape[0]
print(p25)


p26 = titanic.query('Age >= 25 and Age < 35 and Sex=="male" and Survived==1').shape[0]
print(p26)

p27 = titanic.query('Age >= 25 and Age < 35 and Sex=="male" and Survived==0').shape[0]
print(p27)

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Create Columns --------------------------------------------

is_minor = titanic['Age'] < 18
print(type(is_minor))

titanic['is_minor'] = is_minor
titanic['is_minor'] = titanic['Age'] < 18

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- groupby Sigle ---------------------------------------------

titanic.query('Pclass==1').shape[0]
titanic.query('Pclass==2').shape[0]
titanic.query('Pclass==3').shape[0]


grouped_df = titanic.groupby('Pclass')

print(type(grouped_df))
print(grouped_df.size())

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- groupby  Multiple-------------------------------------------

grouped_df = titanic.groupby(['Embarked', 'Pclass'])
summary = grouped_df.agg([np.size, np.mean])['Fare']

print(summary)
print(type(summary))
print(summary.index)

print(summary.loc['C'])
print(summary.loc['C', 1])

summary_noindex = summary.reset_index()
summary_noindex.query('Embarked in ["Q","S"] and Pclass == 3')

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Wide Vs Long Table-----------------------------------------

Q = titanic.query('Embarked=="Q"').groupby('Sex').size()
C = titanic.query('Embarked=="C"').groupby('Sex').size()
S = titanic.query('Embarked=="S"').groupby('Sex').size()
wide = pd.DataFrame({'C': C, 'Q': Q, 'S': S})
wide.reset_index(inplace=True)
print(wide)



long = pd.melt(wide, id_vars=['Sex'], var_name='Embarked', value_name='pax_count')
print(long)

wide2 = long.pivot(index='Sex', columns='Embarked', values='pax_count')

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Adding columns --------------------------------------------

bio = titanic[['Name', 'Age', 'Sex']]
boarding = titanic[['Pclass', 'Ticket', 'Fare']]
bio.head()



combined = pd.concat([bio, boarding], axis=1)
print(combined.head())

# ----------------------------------------------------------------------------------
# ---------------------- Pandas Reading from Local file-----------------------------
# ---------------------- Merging Data Frames ---------------------------------------

gender_size = titanic.groupby('Sex').size()
gender_survivors = titanic.groupby('Sex').sum()['Survived']

gender_total = pd.DataFrame({'total': gender_size, 'survivors': gender_survivors})
gender_total['sur_rate'] = gender_total['survivors'] / gender_total['total']
gender_class_size = titanic.groupby(['Sex', 'Pclass']).size()
gender_class_survivors = titanic.groupby(['Sex', 'Pclass']).sum()['Survived']
gender_class = pd.DataFrame({'total': gender_class_size, 'survivors': gender_class_survivors})
gender_class['sur_rate'] = gender_class['survivors'] / gender_class['total']
gender_total.reset_index(inplace=True)
gender_class.reset_index(inplace=True)


merged = gender_total.merge(gender_class, on="Sex")
print(merged)

merged = gender_total.merge(gender_class, on="Sex", suffixes=['_gender_all', '_gender_class'])
print(merged)


compare_rates = merged[['Sex', 'Pclass', 'sur_rate_gender_all', 'sur_rate_gender_class']].copy()
compare_rates['class_difference'] = compare_rates['sur_rate_gender_class'] - compare_rates['sur_rate_gender_all']

