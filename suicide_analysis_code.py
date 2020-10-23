#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


sdata = pd.read_csv('suicide_data.csv')


# In[3]:


sdata


# In[4]:


sdata.shape


# In[73]:


sdata.rename(columns={" gdp_for_year ($) ":
                  "gdp_for_year", "gdp_per_capita ($)":
                  "gdp_per_capita"}, inplace=True)
sdata.head()


# In[74]:


sdata.describe()


# In[75]:


sdata.count()


# In[76]:


## We will do data cleaning in the last, when we will use HDI for year if necessary.Rset data are already clean i.e error free. 


# In[77]:


s = sdata['suicides_no'].groupby(sdata.year).sum()
s.plot(figsize=(8,6), linewidth=2, fontsize=10,color='black')
plt.xlabel('year', fontsize=15)
plt.ylabel('suicides_no',fontsize=15)


# In[78]:


## The above graph shows the number of suicides with respect to the year.
##As we can visualize that from the year 1997 to 2003,the suicides rate is higher due to some reasons.


# In[79]:


## Number of suicides in 1985
s_year = sdata[(sdata['year'] == 1985)]
s_year = s_year.groupby('country')[['suicides_no']].sum().reset_index()

## Sorting values in ascending order
s_year = s_year.sort_values(by='suicides_no', ascending=False)


# In[80]:


s_year


# In[81]:


## From above we can see the number of suicides in a particular year in a particular states.


# In[82]:


s_year = sdata[(sdata['year'] == 2016)]
s_year = s_year.groupby('country')[['suicides_no']].sum().reset_index()
s_year = s_year.sort_values(by='suicides_no', ascending=False)
s_year


# In[83]:


ax = plt.subplots(1,1,figsize=(13,6))
ax = sns.barplot(x = sdata['generation'], y = 'suicides_no',
                  hue='sex',data=sdata, )


# In[84]:


## The above figure shows the number of suicides with respect to the generation.


# In[85]:


ax = plt.subplots(1,1,figsize=(13,6))
ax = sns.barplot(x = sdata['age'], y = 'suicides_no',
                  data=sdata, )


# In[86]:


## The above figure shows the number of suicides with respect to the age.


# In[87]:


ax = plt.subplots(1,1,figsize=(13,6))
ax = sns.barplot(x = sdata['age'], y = 'suicides_no',
                  hue='sex',data=sdata, )


# In[88]:


##These barplots show that generation of boomers have the highest suicide rate, 
## males in general are more likely to commit suicides than females as well as people from age groups 35-54 yrs and 55-74 yrs


# In[89]:


## Correlation of features
a = plt.subplots(1,1,)
a = sns.heatmap(sdata.corr(),annot=True, cmap='coolwarm')


# In[90]:


e = sdata['suicides_no'].groupby(sdata.country).sum().sort_values(ascending=False)
a = plt.subplots(1,1,figsize=(10,20))
a = sns.barplot(e.head(20), e.head(20).index,)


# In[91]:


##The highest number of suicides is in Russian Federation


# In[92]:


## Suicides number by year
s_year = sdata.groupby('year')[['suicides_no']].sum().reset_index()
s_year.sort_values(by='suicides_no', ascending=False)


# In[93]:


## The highest number of suicides was in 1999 and the lowest in 2016


# In[94]:


## Suicides number by age group
s_age = sdata.groupby('age')[['suicides_no']].sum().reset_index()
s_age.sort_values(by='suicides_no', ascending=False)


# In[95]:


## People committed suicides more in age group 35-54 and 55-74 


# In[101]:


## Relationship between gdp for year and number of suicides
a = plt.subplots(1,1, figsize=(8,8))
a = sns.scatterplot(x="gdp_for_year", y="suicides_no", data=sdata, color='purple')


# In[102]:


## The relationship between "gdp_for_year" and "suicides_no" is not linear. 
## Hence, suicide rate does not depend upon gdp directly.


# In[103]:


## Relationship between gdp per capita and number of suicides
a = plt.subplots(1,1, figsize=(10,8))
a = sns.scatterplot(x="gdp_per_capita", y="suicides_no", data=sdata)


# In[104]:


## Since HDI for year is continious, we can fill those missing values with mean values.


# In[106]:


sdata.fillna(sdata.mean(), inplace=True)


# In[108]:


sdata.count()


# In[110]:


## Relationship between Hdi and number of suicides
a = plt.subplots(1,1, figsize=(10,8))
a = sns.scatterplot(x="HDI for year", y="suicides_no", data=sdata,)


# In[ ]:


##   After analysis,we can conclude that from the year 1997 to 2003,the suicide rates increaded due to some reasons.
##   We can see that generation of boomers have the highest suicide rate and also the males in general
##   are more likely to commit suicides than females as well as people from age groups 35-54 yrs and 55-74 yrs.
##   The other important thing that we noticed, the relationship between "GDP" and "SUCIDE" as well as
##   "HDI" and "SUICIDE"is not linear.which shows that GDP and HDI does not have much impact on suicide rate.

##  AKHIL BHALL

