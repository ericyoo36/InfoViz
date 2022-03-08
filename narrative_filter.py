#!/usr/bin/env python
# coding: utf-8

# # Does Consuming Water/Beverage Before, During, or After Meals Impact Your Caloric Intake?

# In[ ]:





# ---

# Authors: Allysa Alvendia, Adrienne Lee, Michael Wong, Seongmok Yoo

# ---

# In today’s society, there are various social meida outlets that recommends us to follow ambiguous tips on how to maintain a healthy diet. One of them which caught our interest, was the encouragement of drinking lots of water throughout the day. Their reasoning was that it will provide many benefits to our bodies, and as well as reducing our appetite to prevent us from over consuming.

# We decided to investiage this topic in order to see if their claim will actually have an impact on our calorie intake. We came up with a research question to lead this investigation: Is there a relationship between drink consumption and caloric intake from meals?

# Our prediction on this claim is that, with an increased of water/beverage consumption, it will reduce our appetite and our overall caloric intake from our meals.

# Let us explore this claim together through our data and our process of interpretion to determine if there is a relations between water/beverage intake and number of calories consumed.

# ## LET US EXPLORE THE DATA

# In[12]:


# I just imported everything, remove the ones we dont need

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
from datetime import datetime as dt
import altair as alt

get_ipython().run_line_magic('matplotlib', 'inline')


# Here is a sample of our raw data. As one would imagine, it is very difficult to visualize what this data would look like.

# In[13]:


fare_df = pd.read_excel('Phase4.xlsx')

fare_df.sample(5)


# This is the data we have collected over a 7 day period to be explored in depth in relation to our research question.

# There are multiple columns in this dataset but we are only interested in specific columns.

# The **Who**, **What**, **When**, and **Why**

# In[14]:


selection = fare_df.loc[:,['Date', 'Time', 'Name', 'Types of drinks', 'Why did I drink this', 'Total calories in meal (cal)', 'Meal of the day']]

selection


# ## Who?
# The individuals who collected their own eating and drinking habits.

# In[15]:


fare_df['Name'].unique().tolist()


# ## What?
# What did we collect? </br>
# We collected data on the types of beverages consumed and the total number of calories per meal

# In[16]:


fare_df[['Types of drinks', 'Total calories in meal (cal)', 'Meal of the day']].sample(5)


# ### How did we calculate our calories? 
# We used an app called FatSecret. </br>
# As with most calorie tracker apps, there are a lot of variations and options available for counting calories. Total accuracy was not a concern for our data since we only need it to see if there are trends.

# ## When?
# The data collection period, October 13th to October 19th.</br>
# The time when we ate our meals at or when we drank water/beverage.

# In[17]:


fare_df[['Date', 'Time']].sample(5)


# ## Why?
# Why did we drink what we drank?</br>
# Could range from thirst, nutrition, habit, rinise, craving, unwinding, enjoyment, or taste

# In[18]:


fare_df['Why did I drink this'].unique().tolist()


# ## LETS EXPLORE THE VISUALIZATION

# In[19]:


df = pd.read_excel("Phase4.xlsx")

df['Count of who we ate with'] = df['Who we ate with'].str.count(",") + 1
df['Time']= df['Time'].astype(str)
df['Date Time'] = [str(x) + ' ' + y for x, y in zip(df['Date'], df['Time'])]
df = df.sort_values(by=["Date Time"])

ndf = df
ndf['Meal of the day'] = ndf['Meal of the day'].fillna("")
ndf['Date Meal'] = [str(x) + ' ' + y for x, y in zip(ndf['Date'], ndf['Meal of the day'])]

ndf['Drinks before meal'] = 0 

n = 0 
count = {"Adrienne": 0, "Allysa":0, "Eric":0, "Michael":0}
day = ndf.loc[n,"Date"]
for col in ndf["Drinks before meal"]:
    
    if day != ndf.loc[n,"Date"]:
        count["Michael"] = 0 
        count["Adrienne"] = 0
        count["Allysa"] = 0
        count["Eric"] = 0
        day = ndf.loc[n,"Date"]
        
        
    if ndf.loc[n,"Name"] == "Michael" and ndf.loc[n,"Meal of the day"] == "":
        count["Michael"] += 1
        ndf.loc[n,"Drinks before meal"] = count["Michael"]
        
    if ndf.loc[n,"Name"] == "Michael" and ndf.loc[n,"Meal of the day"] != "":
        
        ndf.loc[n,"Drinks before meal"] = count["Michael"]
        count["Michael"] = 0 
        
    if ndf.loc[n,"Name"] == "Adrienne" and ndf.loc[n,"Meal of the day"] == "":
        count["Adrienne"] += 1
        ndf.loc[n,"Drinks before meal"] = count["Adrienne"]
        
    if ndf.loc[n,"Name"] == "Adrienne" and ndf.loc[n,"Meal of the day"] != "":
        
        ndf.loc[n,"Drinks before meal"] = count["Adrienne"]
        count["Adrienne"] = 0

    if ndf.loc[n,"Name"] == "Allysa" and ndf.loc[n,"Meal of the day"] == "":
        count["Allysa"] += 1
        ndf.loc[n,"Drinks before meal"] = count["Allysa"]
        
    if ndf.loc[n,"Name"] == "Allysa" and ndf.loc[n,"Meal of the day"] != "":
        
        ndf.loc[n,"Drinks before meal"] = count["Allysa"]
        count["Allysa"] = 0
        
    if ndf.loc[n,"Name"] == "Eric" and ndf.loc[n,"Meal of the day"] == "":
        count["Eric"] += 1
        ndf.loc[n,"Drinks before meal"] = count["Eric"]
        
    if ndf.loc[n,"Name"] == "Eric" and ndf.loc[n,"Meal of the day"] != "":
        
        ndf.loc[n,"Drinks before meal"] = count["Eric"]
        count["Eric"] = 0
    
    n += 1
    
ndf = ndf[ndf['Who we ate with'].notnull()]
group_ndf = ndf.groupby("Date Meal", as_index=False).sum()
group_ndf["Avg drinks before meal"] = group_ndf["Drinks before meal"]/4 
group_ndf["Avg Calories"] = group_ndf["Total calories in meal (cal)"]/4 


# In[20]:


source = group_ndf

base = alt.Chart(source).mark_bar().encode(
    alt.X('Date Meal', axis=alt.Axis(title=None))
)

area = base.mark_area(opacity=0.3, color='#57A44C').encode(
    alt.Y('Avg Calories',
          axis=alt.Axis(title='Avg. Temperature', titleColor='#57A44C')),
    alt.Y2('Avg drinks before meal')
)

line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
    alt.Y('Avg drinks before meal',
          axis=alt.Axis(title='Precipitation (inches)', titleColor='#5276A7'))
)

alt.layer(area, line).resolve_scale(
    y = 'independent'
)


# In[21]:


# group_ndf.head()
group_ndf['Meal Type'] = ""
i = 0 
for row in group_ndf['Date Meal']:
    ls = group_ndf.loc[i, 'Date Meal'].split()
    group_ndf.loc[i, 'Meal Type'] = ls[-1]
    i+= 1
group_ndf.head(50)


# In[23]:


# Zoom - Not that useful in our case
base = alt.Chart(source).encode(x='Date Meal')

bar = base.mark_bar().encode(y='Avg Calories').interactive()

line =  base.mark_line(color='red').encode(
    y='Avg drinks before meal'
).interactive()

top = (bar + line).properties(width=600)
alt.layer(bar, line).resolve_scale(
    y = 'independent'
)


# In[24]:


# Filter with line, but other y-axis is gone
selection = alt.selection_multi(fields=['Meal Type'])
base = alt.Chart(source).encode(x='Date Meal')

bar = base.mark_bar().encode(y='Avg Calories')

line =  base.mark_line(color='red').encode(
    y='Avg drinks before meal'
)

top = (bar + line).properties(width=600).transform_filter(
    selection
)
alt.layer(bar, line).resolve_scale(
    y = 'independent'
)

bottom = alt.Chart().mark_bar().encode(
    x='Meal Type',
    y='Avg Calories',
    color=alt.condition(selection, alt.value('steelblue'), alt.value('lightgray'))
).properties(
    width=600, height=100
).add_selection(
    selection
)

alt.vconcat(
    top, bottom,
    data=source
)


# In[25]:


# FILTER 

selection = alt.selection_multi(fields=['Meal Type'])

top = alt.Chart().mark_bar().encode(
    x='Date Meal',
    y='Avg Calories'
).properties(
    width=600, height=200
).transform_filter(
    selection
)



bottom = alt.Chart().mark_bar().encode(
    x='Meal Type',
    y='Avg Calories',
    color=alt.condition(selection, alt.value('steelblue'), alt.value('lightgray'))
).properties(
    width=600, height=100
).add_selection(
    selection
)

alt.vconcat(
    top, bottom,
    data=source
)


# In[26]:


# Details on Demand
selector = alt.selection_single(empty='all', fields=['Date Meal'])
base = alt.Chart(source).add_selection(selector)



# .properties(
# #     width=250,
# #     height=250
# ).add_selection(selector)

# points = base.mark_bar().encode(
#     x='Date Meal',
#     y='Avg Calories',
#     color=alt.condition(selector, 'id:O', alt.value('lightgray'), legend=None),
# )

bar = base.mark_bar().encode(
      x='Date Meal',
      y='Avg Calories',
      color=alt.condition(selector, 'id:O', alt.value('lightgray'), legend=None)
)



# line =  base.mark_line(color='red').encode(
#     y='Avg drinks before meal'
# )

# top = (bar + line).properties(width=600)
# alt.layer(bar, line).resolve_scale(
#     y = 'independent').add_selection(selector)

more_detail = base.mark_bar().encode(
    x='Date Meal',
    y= 'Total calories in meal (cal)', #alt.Y('Total calories in meal (cal)', scale=alt.Scale(domain=(-15, 15))),
    color=alt.Color('id:O', legend=None)
).transform_filter(
    selector
)

bar | more_detail


# In[27]:


# Not working
selector = alt.selection_single(empty='all', fields=['Date Meal'])
base = alt.Chart(source)



# .properties(
# #     width=250,
# #     height=250
# ).add_selection(selector)

# points = base.mark_bar().encode(
#     x='Date Meal',
#     y='Avg Calories',
#     color=alt.condition(selector, 'id:O', alt.value('lightgray'), legend=None),
# )

bar = base.mark_bar().encode(
    x='Date Meal',
      y='Avg Calories',
      color=alt.condition(selector, 'id:O', alt.value('lightgray'), legend=None)
)



line =  base.mark_line(color='red').encode(
    x ='Date Meal',
    y='Avg drinks before meal'
)

# top = (bar + line).properties(width=600)
alt.layer(bar, line).resolve_scale(
    y = 'independent').add_selection(selector)

# timeseries = base.mark_bar().encode(
#     x='Date Meal',
#     y= 'Total calories in meal (cal)', #alt.Y('Total calories in meal (cal)', scale=alt.Scale(domain=(-15, 15))),
#     color=alt.Color('id:O', legend=None)
# ).transform_filter(
#     selector
# )

# timeseries
# top | timeseries


# In[ ]:


# Not working
selector = alt.selection_single(empty='all', fields=['Date Meal'])
base = alt.Chart(source).add_selection(selector)

bar = base.mark_bar().encode(
    x='Date Meal',
    y='Avg Calories',
    color=alt.condition(selector, 'id:O', alt.value('lightgray'), legend=None)
)

# line =  base.mark_line(color='red').encode(
#     x ='Date Meal',
#     y='Avg drinks before meal'
# )

# top = (bar + line).properties(width=600).add_selection(selector)
# alt.layer(bar, line).resolve_scale(
#     y = 'independent')

timeseries = base.mark_bar().encode(
    x='Date Meal',
    y= 'Total calories in meal (cal)', #alt.Y('Total calories in meal (cal)', scale=alt.Scale(domain=(-15, 15))),
    color=alt.Color('id:O', legend=None)
).transform_filter(
    selector
)

top | timeseries


# In[ ]:


fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date Meal', y='Avg Calories', data = group_ndf, color='#B9DF68')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = '#8B66DE'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date Meal', y='Avg drinks before meal', data = group_ndf, sort=False, color=color, marker="o")
ax2.tick_params(axis='y', color=color)
plt.show()


# Theis visualization shows us the overall averaged comparison between our calorie intake and drink consumption. 

# For calories, it is a calculated average of the meals of the four members. As shown by the lime green bars of the bar chart. 

# Overlaying on top of that, it is the average number of drinks consumed before each meal. As show by a purple line graph.

# ## Counting Drinks
# We are only counting the number of drinks consumed before meals.

# To get a better representation of the overall sample, we took an average of the number of consumed drinks before each meal. With this, we are now able to see if a trend exists between the number of drinks consumed and the number of calories consumed per meal.

# With this, we are able to visualize if there is a relationship between drink consumption and the number of caloric intake from meals.

# ## Meal Types
# different meal of the day might have its own relation between the calorie intake and drink consumption

# We will take a specific look at our breakfast, lunch, and dinner to see if it has a unique trend

# In[ ]:


df_filter = group_ndf.loc[group_ndf['Date Meal'].isin(['10/13 breakfast','10/14 breakfast','10/15 breakfast','10/16 breakfast','10/17 breakfast','10/18 breakfast','10/19 breakfast'])]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date Meal', y='Avg Calories', data = df_filter, color='#B9DF68')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = '#8B66DE'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date Meal', y='Avg drinks before meal', data = df_filter, sort=False, color=color, marker="o")
ax2.tick_params(axis='y', color=color)
plt.show()


# This visualization is filtered for breakfast.

# Here, We notice that the average calorie intake for breakfasts have very little variation throughout the 7 day period.</br>
# Also, for the average drink consumption, the most is 1 drink before meal.

# In[ ]:


df_filter = group_ndf.loc[group_ndf['Date Meal'].isin(['10/13 lunch','10/14 lunch','10/15 lunch','10/16 lunch','10/17 lunch','10/18 lunch','10/19 lunch'])]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date Meal', y='Avg Calories', data = df_filter, color='#B9DF68')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = '#8B66DE'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date Meal', y='Avg drinks before meal', data = df_filter, sort=False, color=color, marker="o")
ax2.tick_params(axis='y', color=color)
plt.show()


# This visualization is filtered for lunch.

# Here, there is a big diffrence from day to day in the average calories and drinks consumption.

# Due to this huge variations, we are unable to the determine if there is a trend if drinking more will lead us to eat less.

# In[ ]:


df_filter = group_ndf.loc[group_ndf['Date Meal'].isin(['10/13 dinner','10/14 dinner','10/15 dinner','10/16 dinner','10/17 dinner','10/18 dinner','10/19 dinner'])]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date Meal', y='Avg Calories', data = df_filter, color='#B9DF68')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = '#8B66DE'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date Meal', y='Avg drinks before meal', data = df_filter, sort=False, color=color, marker="o")
ax2.tick_params(axis='y', color=color)
plt.show()


# This visualization is filtered for dinner.

# Here, there is also a big diffrence from day to day in average calories and drinks consumption as well.
# 
# In comparison to dinner, we ate less than half of the calories for dinner and a bit smaller for our lunches

# If there is a correlation between water/beverage and calorie consumption, it is difficult to tell due to the huge variations in between.

# ## HABITS
# could be relevant in seeing if there is a trend with the number of caloric intake

# ### Why?
# It could affect the number of calories we consume

# BEFORE: increase fullness before meals

# AFTER: unconscious decrease food intake to accommodate beverage intake

# for
# ### NUTRITION
# there is a set time when it is consumed and the timing of the consumption could affect overall appetite and/or caloric intake

# In[1]:


# viz filter for habits?


# ## Closer Look at the Types of Water/Beverages Consumed versus How Much More We Ate

# In[ ]:


# viz on those two??


# ### BEVERAGE CONSUMPTION 
# is very dependent on personal habits and nutritional intake. This could be misleading when looking for a trend

# ### CALORIC INTAKE
# is only based on the three main meals which could leave out a lot of other calories, such as snacks or an extra meal. 

# In[ ]:


# need the visualization to do comparison and contrast]


# In[ ]:


#viz


# In[28]:


selection = alt.selection_single(empty = 'all')

base = alt.Chart(group_ndf).encode(x = 'Date Meal')
bar = base.mark_bar(color='#B9DF68').encode( y = alt.Y('Avg Calories', title = 'Avg. Calories (kcal)'), 
                                            color = alt.condition(selection, alt.value('#B9DF68'), alt.value('lightgray')))
line = base.mark_line(point = True, color='#8B66DE').encode(y = 'Avg drinks before meal', color = alt.condition(selection, alt.value('#8B66DE'), alt.value('lightgray')))


alt.layer(bar,line).resolve_scale(y='independent').properties(title = 'Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals').add_selection(selection).encode(tooltip = [alt.Tooltip('Avg Calories', type = 'quantitative'), alt.Tooltip('Avg drinks before meal', type = 'quantitative')])


# # Conclusion

# Remember our predication at the beginning? We predicted that drinking more will reduce our appetite.
# Let us see if this was the case. 

# Through the exploration our data and visualizations together, we can conclude that there is no meaningful or supportive evidence that when we consume water/beverages have an impact on calorie consumption.

# There is one trend that we noticed is that there is that we drink and eat less in the mornings. 
# But then towards the end of the day, there is an increased of drink consumption and calorie intake.
# Which is quite an interesting insight.

# In conclusion, our assumption was wrong!

# Due to the limitations of the data and possible inaccuracy of our data collection process, we cannot definitively say that the water/beverage consumption will reduce our appetite as claimed by social media.
