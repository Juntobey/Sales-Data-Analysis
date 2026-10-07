#!/usr/bin/env python
# coding: utf-8

# Sales Data

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_excel( r"C:\Users\lebog\Downloads\Happy data project\Sales.xlsx")


# In[3]:


df = dataset


# In[4]:


df.head()


# In[5]:


df.drop_duplicates()


# In[6]:


null = pd.isnull(df)
null.head()


# In[9]:


pd.isnull(df).sum().sum()


# In[7]:


print(df.columns)


# In[8]:


type(df.Order_Date[0])


# In[9]:


df.info()


# In[17]:


df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce', dayfirst=True)


# In[18]:


print(df)


# In[15]:


df.info()


# In[16]:


df.head(10)


# In[ ]:




