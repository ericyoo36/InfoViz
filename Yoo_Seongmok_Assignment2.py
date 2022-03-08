#!/usr/bin/env python
# coding: utf-8

# # Calgary's Emergency Shelters and its relation to Temperature

# CPSC 583 Assignment 2
# Seongmok, Yoo(Eric)
# 10162624

# This notebook is about learning the relationship  between homelessness and weather conditions in Calgary, Alberta. Original question I have is if weather is colder, will there be more homeless in the shelter. In other words, during warm weather will there be more homeless on the streets instead of shelter. In this notebook, approperiate dataset and visulization of them will be presented to  verifiy the original question. 

# 1)	From the dataset, the missing data is Inn From the Cold – Family Shelter’s 2nd floor overflow total overnight. Since this shelter has one room with capacity of four, it’s the only shelter which has 0 total overnight through out the dataset. 

# 4a)

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# 4b)

# In[2]:


all_df = pd.read_excel("May-2021-Calgary-Emergency-Shelters.xlsx")


# 4c)

# In[3]:


temp_df = all_df[['Day', 'Actual High Temp', 'Actual Low Temp']]


# In[4]:


shelters_df = (all_df[all_df.columns[3:47]]).head(5) 


# 4d)

# In[5]:


all_df['Day'] = all_df['Day'].dt.strftime('%m/%d')


# In[6]:


print(all_df.head(5))


# 4e)

# In[7]:


all_df['CDIC-River Front avg'] = (all_df['CDIC - River Front (Combined) Overnight'] / all_df['CDIC - River Front (Combined) Capacity']) * 100


# In[8]:


all_df['CDIC-Hillhurst avg'] = (all_df['CDIC - Hillhurst Centre 2507 - Emergency Overnight'] / all_df['CDIC - Hillhurst Centre 2507 - Emergency Capacity']) * 100


# In[9]:


all_df['CDIC-Days Inn avg'] = (all_df['CDIC - Days Inn Overflow Overnight'] / all_df['CDIC - Days Inn Overflow Capacity']) * 100


# In[10]:


all_df['CDIC-Main Site avg'] = (all_df['CDIC - Main Site Overnight'] / all_df['CDIC - Main Site Capacity']) * 100


# In[11]:


print(all_df.head(5))


# 5a)

# In[23]:


barchart_5a=sns.barplot(x='Actual High Temp', y='Day', data=all_df.head(7))


# 5b)

# In[22]:


barchart_5b=sns.barplot(x='Actual High Temp', y='Day', data=all_df)


# 5c)

# In[25]:


barchart_5c=sns.barplot(x='Actual Low Temp', y='Day', data=all_df)


# 5d)

# In[36]:


linechart_5d=sns.lineplot(x='Day', y='CDIC-River Front avg', data=all_df)


# 5e) 

# In[37]:


print(all_df[['Day','Actual Low Temp','CDIC-River Front avg','CDIC-Hillhurst avg','CDIC-Days Inn avg','CDIC-Main Site avg']])


# since the coldest day was May 10th with lowest temperature of -3, percentage of occupancy for each CDIC shelters are 85% for River Front, 91% for Hillhurst, 61% for Days Inn, and 29% for Main Site.

# 5f)

# In[35]:


linechart_5f1=sns.lineplot(x='Day', y='CDIC-Hillhurst avg', data=all_df)


# In[34]:


linechart_5f2=sns.lineplot(x='Day', y='CDIC-Days Inn avg', data=all_df)


# In[33]:


linechart_5f3=sns.lineplot(x='Day', y='CDIC-Main Site avg', data=all_df)


# 5g)

# In[65]:


linechart_5d=sns.lineplot(x='Day', y='CDIC-River Front avg', data=all_df.head(10), linewidth=2.5, color='red',)


# In this line graph, I have change line leght to be more thicker than the deafult, and chaged the line color to be more viewable. Also range of days have been changed to first 10 days of May to track its increase period.

# In[66]:


sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
linechart_5f1=sns.scatterplot(x='Day', y='CDIC-Hillhurst avg', data=all_df)


# In this graph, I have changed it to a scatter graph by removing lines. I have also changed the back ground to a grid which makes it easier to track each point's value. Also graph's size has been increased for easier view on it.

# In[67]:


linechart_5f2=sns.lineplot(x='Day', y='CDIC-Days Inn avg', data=all_df)
plt.xlabel("Days (mm/dd)", fontsize= 12)
plt.ylabel("Average occupancy", fontsize= 12)
plt.title("Average Occupancy of CDIC-Days Inn location", fontsize= 15)


# In this graph I have added a title and labels for x and y axis so that the graph is more clear in its delivering what its about to viewers.

# In[69]:


linechart_5f3=sns.lineplot(x='Day', y='CDIC-Main Site avg', data=all_df,linewidth=3, color='black')
plt.xlabel("Days (mm/dd)", fontsize= 12)
plt.ylabel("Average occupancy", fontsize= 12)
plt.title("Average Occupancy of Main Site location", fontsize= 15)


# In this graph, all changes made to previous graphs are combined into one to produce best apealing and readable line graph. Changes include, addition of title, x axis label, y axis label, size increase, backrough grid, line thinckness, and line color. 

# 6) after looking at 4 line charts representing the average occupancy of CDIC shelters, at first glance, they look significantly different from each other. For example, Days Inn, and Hillhurst locations have a up spkie near the end of May, but River Front and Main Site locations have a down spike. If looked in different angle, they have some similar characteristics also. In the last week of May all 4 locations have reached its lowest average occupancy. This could be an result of having a relatively warmer weather in that time period. 

# 7) To ensure a more comprehensive analysis of emergency shelter occupancy in Calgary, I strongly feel that data variables that could show dramatic difference is needed. for example, Average occupancy related to weather condition needs to based on months of the year not daily. This will show more significant difference in average temperature. Also, weather conditions should contain more data variables, other than just temperature. Whether it rained or snowed or stormed might also effect average occupancy of homeless shelters in Calgary. To compare emergency shelter usage more correctly, data variable about where homeless are staying if not using a shelter would also be useful. 
# 
# Using occupancy rate of shelter is not a good estimation for homelessness. The reason is that it does not represent the whole popuplation that is homeless. There might be homeless people on the streets, or form a group to live on somewhere else. Therefore, insight we can gain through looking at shelter occupancy is very limited. 
# 
# Also, It does not give us insights on what causes homelessness. Cause of homelessness is more strongly related to each individual's backgroud and history. To gain an idea of what might cause homelessness, detailed research on inividual is needed. whether or not they use emergency shelter depending on the weather condition does not provide us with that kind of information. 
# 
# To gain knowledge of homelessness problem, I would set up a dataset about homeless people past. In this case, data collection on their age, family members, years spent as homeless, average earnings, and ethnic group. Since to find out why people are being homeless, it is important to track how they lived before being a homeless. Limitation to this dataset would be there has to be data collection on each individual. This requires alot more time and effort. Also it is hard to find every homeless people around the city. 
