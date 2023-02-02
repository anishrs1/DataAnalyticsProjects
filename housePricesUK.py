# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:26:16 2023

@author: anish
"""

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats
import re
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

house = pd.read_csv('C:/Users/anish/Downloads/Average_UK_houseprices_and_salary.csv')
house.head()

income = pd.read_csv('C:/Users/anish/Downloads/Income_by_age_and_gender.csv')
income.head()

house.info()

house.columns

house.shape

house.describe()

house.isna().sum()

house.Year.unique()

house['Average house price adj. by inflation (pounds)'].unique()

house['Median Salary adj. by inflation (pounds)'].unique()

house['Unnamed: 3'].unique()

income.head()

income.info()

income.describe(include=object)
income.describe(include='all')

income.isna().sum()

income['Age group'].unique()

income['Median salary (pounds)'].unique()

income['Gender'].unique()

house.columns

house.drop('Unnamed: 3', axis=1, inplace=True)

house.columns

house.columns = [x.rsplit(' ', 4)[0] for x in house.columns]
# shorten column names to only first two words
house.columns = [re.sub(r'\s+', '_', x).lower() for x in house.columns]
# replace spaces with underscores, make all characters lowercase
house.columns

income.columns = [x.rsplit(' ', 1)[0] for x in income.columns]
# shorten column names to only first two words
income.columns = [re.sub(r'\s+', '_', x).lower() for x in income.columns]
# replace spaces with underscores, make all characters lowercase
income.columns

house.dropna(inplace=True)

house

sns.boxplot(x=house.median_salary)
plt.show()

sns.boxplot(x=house.average_house_price)
plt.show()

sns.boxplot(x=income.median_salary)
plt.plot()
plt.show()

income

sns.histplot(house.average_house_price)

plt.figure(figsize=(25,9))
sns.regplot(data=house, x='year', y='average_house_price', scatter_kws={"s": 100}, ci=15)
plt.title('UK Average House Prices (1975-2020)')
plt.xlabel('Year')
plt.ylabel('Average house price adj. by inflation (pounds)')
plt.plot()
plt.show()

slope, intercept = np.polyfit(house.year, house.average_house_price, 1)

print('Average house price adj. by inflation have gone up by: £' + str(round(slope, 2)))

plt.figure(figsize=(25,9))
sns.regplot(data=house, x='year', y='median_salary', scatter_kws={"s": 100}, ci=15)
plt.title('UK Median Salary (1975-2020)')
plt.xlabel('Year')
plt.ylabel('Median Salary adj. by inflation (pounds)')
plt.show()

slope, intercept = np.polyfit(house.year, house.median_salary, 1)

print('Median Salary adj. by inflation have gone down by: £' + str(round(slope, 2)))

plt.figure(figsize=(25,9))
sns.histplot(house.median_salary)
plt.show()

plt.figure(figsize=(25,9))
sns.barplot(data=income, x='median_salary', y='age', hue='gender')
plt.title('UK Median Salary (1975-2020)')
plt.xlabel('Median Salary adj. by inflation (pounds)')
plt.ylabel('Age Group')
plt.show()

income.groupby(['age','gender']).sum()

fifty = income[income['age'].isin(['50 to 59'])]

fifty

sns.barplot(x=fifty.age, y=fifty.median_salary, hue=fifty.gender)

fifty[fifty['age'].isin(['50 to 59'])]['median_salary'].diff()