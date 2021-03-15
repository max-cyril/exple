#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip


# In[2]:


#pip install vega_datasets


# In[10]:


from vega_datasets import data
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


# In[18]:


data.list_datasets()
df=data.iris()
df.head()


# In[19]:


expal = ProfileReport(df, title="Pandas Profiling Report",explorative=True)
expal


# In[20]:


expal.to_widgets()


# In[15]:


expal.to_notebook_iframe()


# In[21]:


expal.to_file("your_report.html")#If you want to generate a HTML report file, save the ProfileReport to an object and use the to_file() function:


# In[ ]:


# As a string
json_data = expal.to_json()

# As a file
expal.to_file("your_report.json")

