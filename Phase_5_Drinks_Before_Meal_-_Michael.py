#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.ticker as ticker


# In[2]:


df = pd.read_excel("_Phase4.xlsx")
df.head()


# In[3]:


# newdf = df.query('`Who we ate with` == ""')

# newdf.head()
# df = df[df['Who we ate with'].notnull()]
df.head(20)

df['Count of who we ate with'] = df['Who we ate with'].str.count(",") + 1
df['Time']= df['Time'].astype(str)
df['Date Time'] = [str(x) + ' ' + y for x, y in zip(df['Date'], df['Time'])]
df = df.sort_values(by=["Date Time"])


# In[4]:


ndf = df
ndf['Meal of the day'] = ndf['Meal of the day'].fillna("")
ndf['Date Meal'] = [str(x) + ' ' + y for x, y in zip(ndf['Date'], ndf['Meal of the day'])]

ndf['Drinks before meal'] = 0 
ndf.head(30)


# In[5]:


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
ndf.head(30)


# In[39]:


ndf = ndf[ndf['Who we ate with'].notnull()]
group_ndf = ndf.groupby("Date Meal", as_index=False).sum()
group_ndf["Avg drinks before meal"] = group_ndf["Drinks before meal"]/4 
group_ndf["Avg Calories"] = group_ndf["Total calories in meal (cal)"]/4 
group_ndf.head(50)


# In[40]:


fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=65, horizontalalignment="center")
ax1.set_title('Avg. Calorie Intake Per Meal by Avg. Drinks Consumed Before Meals', fontsize=16)
ax2 = sns.barplot(x='Date Meal', y='Avg Calories', data = group_ndf, color='tab:green')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg. Drinks Before Meal', fontsize=16, color=color)
ax1.set_xlabel('Date Meal', fontsize=16)
ax1.set_ylabel('Avg. Calories (kcal)', fontsize=16)
ax2 = sns.lineplot(x='Date Meal', y='Avg drinks before meal', data = group_ndf, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# In[ ]:




