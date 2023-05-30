import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())
print(census.dtypes)
census['birth_year'] = census['birth_year'].replace('missing', '1967')
census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)
print(census['birth_year'].unique())
print("Average Birth Year: ",census['birth_year'].mean())
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)
print(census['higher_tax'].unique())
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())
#census = pd.get_dummies(census, columns=['marital_status'])
print(census.head())
current_year = 2023
age = []
for i in census['birth_year']:
  age.append(current_year-i)
census['age'] = age
#print(max(age))
#print(min(age))
#age_group = ['15-20','21-25','26-30','31-35','36-40','41-45','46-50','51-55','56-60','61-65','66-70','71-75','76-80','81-85']
age_group = []
for i in census['age']:
  if i >= 15 and i <=20:
    age_group.append('15-20')
  elif i >=21 and i <=25:
    age_group.append('21-25') 
  elif i >=26 and i <=30:
    age_group.append('26-30') 
  elif i >=31 and i <=35:
    age_group.append('31-35') 
  elif i >=36 and i <=40:
    age_group.append('36-40')
  elif i >=41 and i <=45:
    age_group.append('41-45')  
  elif i >=46 and i <=50:
    age_group.append('46-50') 
  elif i >=51 and i <=55:
    age_group.append('51-55') 
  elif i >=56 and i <=60:
    age_group.append('56-60') 
  elif i >=61 and i <=65:
    age_group.append('61-65') 
  elif i >=66 and i <=70:
    age_group.append('66-70') 
  elif i >=71 and i <=75:
    age_group.append('71-75') 
  elif i >=76 and i <=80:
    age_group.append('76-80') 
  elif i >=81 and i <=85:
    age_group.append('81-85') 
#print(census.head())
#print(age_group)
census['age_group'] = age_group
census = pd.get_dummies(census, columns=['age_group'])

print(census.head())