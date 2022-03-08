#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
from datetime import datetime as dt
import altair as alt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


all_df = pd.read_excel('coordinates.xlsx')

plt.xlim(600, 1300) 
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .02, edgecolor = 'none', color = 'darkred', s = 1000)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coordinates from CS:GO gameplay (coordinates.txt)', fontsize=16)


# In[13]:


all_df = pd.read_excel('coordinates1.xlsx')


sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .02, edgecolor = 'none', color = 'darkred', s = 1000)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coordinates from CS:GO gameplay(coordinates1.txt)', fontsize=16)


# In[14]:


all_df = pd.read_excel('coordinates2.xlsx')

sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .02, edgecolor = 'none', color = 'darkred', s = 1000)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coordinates from CS:GO gameplay(coordinates2.txt)', fontsize=16)


# In[15]:


all_df = pd.read_excel('coordinates3.xlsx')

sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .02, edgecolor = 'none', color = 'darkred', s = 1000)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coordinates from CS:GO gameplay(coordinates3.txt)', fontsize=16)


# In[16]:


all_df = pd.read_excel('coordinatesconcat.xlsx')

sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .02, edgecolor = 'none', color = 'darkred', s = 1000)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coordinates from CS:GO gameplay(coordinatesconcat.txt)', fontsize=16)


# In[72]:


all_df = pd.read_excel('coordinates.xlsx')
plt.xlim(900, 1000)
plt.ylim(530, 550)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.scatterplot(x='X', y='Y', data=all_df, alpha = .1, edgecolor = 'none', color = 'darkred', s = 700)
viz1.set_xlabel('X coordinate', fontsize=16)
viz1.set_ylabel('Y coordinate', fontsize=16)
viz1.set_title('Mouse position coorinates from CS:GO gameplay', fontsize=16)

sns.kdeplot(x='X', y='Y', data=all_df,cmap="Reds",shade=True)


# In[12]:


all_df = pd.read_excel('intoutput2.xlsx')
vizdf = all_df.sample(50)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput2.txt)', fontsize=16)


# In[11]:


vizdf['output'].tolist()


# In[10]:


all_df = pd.read_excel('intoutput2.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput2.txt)', fontsize=16)


# In[14]:


all_df = pd.read_excel('intoutput3.xlsx')
all_df.sort_values(by=['output'])
vizdf = all_df.tail(100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput3.txt)', fontsize=16)


# In[15]:


all_df = pd.read_excel('intoutput3.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput3.txt)', fontsize=16)


# In[16]:


all_df = pd.read_excel('intoutput4.xlsx')
all_df.sort_values(by=['output'])
vizdf = all_df.tail(100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput4.txt)', fontsize=16)


# In[17]:


all_df = pd.read_excel('intoutput4.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput4.txt)', fontsize=16)


# In[24]:


all_df = pd.read_excel('intoutput5.xlsx')
all_df.sort_values(by=['output'])
vizdf = all_df.tail(100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput5.txt)', fontsize=16)


# In[19]:


all_df = pd.read_excel('intoutput5.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput5.txt)', fontsize=16)


# In[20]:


all_df = pd.read_excel('intoutput6.xlsx')
all_df.sort_values(by=['output'])
vizdf = all_df.tail(100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput6.txt)', fontsize=16)


# In[21]:


all_df = pd.read_excel('intoutput6.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput6.txt)', fontsize=16)


# In[22]:


all_df = pd.read_excel('intoutput7.xlsx')
all_df.sort_values(by=['output'])
vizdf = all_df.tail(100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.countplot(x='output', data=vizdf)
viz1.set_xlabel('Integer Output', fontsize=16)
viz1.set_ylabel('Count', fontsize=16)
viz1.set_title('Integer Output x Count (intoutput7.txt)', fontsize=16)


# In[23]:


all_df = pd.read_excel('intoutput7.xlsx')
plt.xlim(0, 100)
sns.set(style="darkgrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
viz1=sns.lineplot(x='X',y='output', data=all_df, color = '#8B66DE', marker = "o")
viz1.set_xlabel('Index', fontsize=16)
viz1.set_ylabel('Integer Output', fontsize=16)
viz1.set_title('Index x Integer Output (intoutput7.txt)', fontsize=16)


# In[ ]:




