#!/usr/bin/env python
# coding: utf-8

# # Does Consuming Water/Beverage Before, During, or After Meals Impact Your Caloric Intake?

# ---

# Authors: Allysa Alvendia, Adrienne Lee, Michael Wong, Seongmok Yoo

# ---

# In today’s society, there are various social meida outlets that recommends us to follow ambiguous tips on how to maintain a healthy diet. One of them which caught our interest, was the encouragement of drinking lots of water throughout the day. Their reasoning was that it will provide many benefits to our bodies, and as well as reducing our appetite to prevent us from over consuming.

# We decided to investiage this topic in order to see if their claim will actually have an impact on our calorie intake. We came up with a research question to lead this investigation: Is there a relationship between drink consumption and caloric intake from meals?

# Our prediction on this claim is that, with an increased of water/beverage consumption, it will reduce our appetite and our overall caloric intake from our meals.

# Let us explore this claim together through our data and our process of interpretion to determine if there is a relations between water/beverage intake and number of calories consumed.

# ## LET US EXPLORE THE DATA

# In[1]:


# I just imported everything, remove the ones we dont need

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime as dt

get_ipython().run_line_magic('matplotlib', 'inline')


# Here is a sample of our raw data. As one would imagine, it is very difficult to visualize what this data would look like.

# In[2]:


fare_df = pd.read_excel('Phase4.xlsx')

fare_df.sample(5)


# This is the data we have collected over a 7 day period to be explored in depth in relation to our research question.

# There are multiple columns in this dataset but we are only interested in specific columns.

# The Who, What, When, and Why

# In[3]:


# need to be updated with your addition onto Phase4 excel file

selection = fare_df.loc[:,['Date', 'Time', 'Name', 'Types of drinks', 'Why did I drink this', 'Total calories in meal (cal)', 'Meal of the day']]

selection


# needs to be updated after for your addition to the excel file
# 
# ## Who?
# The individuals who collected their own eating and drinking habits

# In[4]:


fare_df['Name'].unique().tolist()


# ## What?
# What did we collect? We collected data on the types of beverages consumed and the total number of calories per meal

# In[5]:


fare_df[['Types of drinks', 'Total calories in meal (cal)', 'Meal of the day']].sample(5)


# ### How did we calculate our calories? 
# We used an app called FatSecret. As with most calorie tracker apps, there are a lot of variations and options available for counting calories. Total accuracy was not a concern for our data since we only need it to see if there are trends.

# ## When?
# - The data collection period, October 13th to October 19th
# - The time when we ate our meals at or when we drank water/beverage

# In[6]:


fare_df[['Date', 'Time']].sample(5)


# ## Why?
# Why did we drink what we drank? Could range from thirst, nutrition, habit, rinise, craving, unwinding, enjoyment, or taste

# In[7]:


fare_df['Why did I drink this'].unique().tolist()


# ## LETS EXPLORE THE VISUALIZATION

# In[36]:


all_df = pd.read_excel("vis.xlsx")
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date', y='Calories', data = all_df, color='tab:green')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date', y='Drinks', data = all_df, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# Above visualization shows us overall comparison between our calorie intake and drink consumption. 

# Average calorie of the meals of 4 members has beeen represented using bar chart in green color. 

# Overlaying on top of that, average number of drinks consumed before each meal has been represented using a line graph in red color.

# ## TIMING
# of beverage consumption is important out whether it has any relationship with the number of calories consumed per meal

# In[23]:


df_filter = all_df.loc[all_df['Meal'] == 'breakfast']
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90, horizontalalignment="center")
ax1.set_title('Avg calorie intake per meal, and Avg drinks consumed before meals', fontsize=16)
ax2 = sns.barplot(x='Date', y='Calories', data = df_filter, color='tab:green')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg Drinks before meal', fontsize=16, color=color)
ax1.set_xlabel('Date/Meal', fontsize=16)
ax1.set_ylabel('Avg Calories', fontsize=16)
ax2 = sns.lineplot(x='Date', y='Drinks', data = df_filter, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# Above visualization is only including data realted to our breakfasts. We noticed that average calorie intake for breakfasts does not change much. Also, for drink consumption, we either drank none or only up to 1 drinks before breakfast.

# In[24]:


df_filter = all_df.loc[all_df['Meal'] == 'lunch']
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90, horizontalalignment="center")
ax1.set_title('Avg calorie intake per meal, and Avg drinks consumed before meals', fontsize=16)
ax2 = sns.barplot(x='Date', y='Calories', data = df_filter, color='tab:green')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg Drinks before meal', fontsize=16, color=color)
ax1.set_xlabel('Date/Meal', fontsize=16)
ax1.set_ylabel('Avg Calories', fontsize=16)
ax2 = sns.lineplot(x='Date', y='Drinks', data = df_filter, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# Above visualization only includes data related to our luches. There are bigger diffrence between day to day in averae calories and drinks consumption, but cannot relate to the trend of drinking more will lead us to eat less.

# In[25]:


df_filter = all_df.loc[all_df['Meal'] == 'dinner']
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90, horizontalalignment="center")
ax1.set_title('Avg calorie intake per meal, and Avg drinks consumed before meals', fontsize=16)
ax2 = sns.barplot(x='Date', y='Calories', data = df_filter, color='tab:green')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg Drinks before meal', fontsize=16, color=color)
ax1.set_xlabel('Date/Meal', fontsize=16)
ax1.set_ylabel('Avg Calories', fontsize=16)
ax2 = sns.lineplot(x='Date', y='Drinks', data = df_filter, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# Above visualization only includes data related to our dinners. 
# There are bigger diffrence between day to day in averae calories and drinks consumption than our breakfasts, but smaller than our lunches. We still could not relate to the trend of drinking more will lead us to eat less.

# ## WHEN
# the beverages are consumed are very important. We are only looking at the three values of WHEN.

# **Before**, **During**, and **After** meals

# For before and after on beverage consumption, we are only counting drinks that are 1 hour before and after only
# 
# ## add your justification here and counting

# In[10]:


# viz filter for drinks?


# ## HABITS
# could be relevant in seeing if there is a trend with the number of caloric intake

# ### Why?
# It could affect the number of calories we consume

# BEFORE: increase fullness before meals

# AFTER: unconscious decrease food intake to accommodate beverage intake

# for
# ### NUTRITION
# there is a set time when it is consumed and the timing of the consumption could affect overall appetite and/or caloric intake

# In[11]:


# viz filter for habits?


# ## Closer Look at the Types of Water/Beverages Consumed versus How Much More We Ate

# In[12]:


# viz on those two??


# ### BEVERAGE CONSUMPTION 
# is very dependent on personal habits and nutritional intake. This could be misleading when looking for a trend

# ### CALORIC INTAKE
# is only based on the three main meals which could leave out a lot of other calories, such as snacks or an extra meal. 

# In[13]:


# need the visualization to do comparison and contrast]


# In[14]:


#viz


# # Conclusion

# Remember our predication at the beginning? We predicted that drinking more will reduce our appetite.
# Let us see if this was the case. 

# Through the exploration our data and visualizations together, we can conclude that there is no meaningful or supportive evidence that when we consume water/beverages have an impact on calorie consumption.

# There is one trend that we noticed is that there is that we drink and eat less in the mornings. 
# But then towards the end of the day, there is an increased of drink consumption and calorie intake.
# Which is quite an interesting insight.

# In conclusion, our assumption was wrong!

# Due to the limitations of the data and possible inaccuracy of our data collection process, we cannot definitively say that the water/beverage consumption will reduce our appetite as claimed by social media.

# 

# In[ ]:




