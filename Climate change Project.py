#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[33]:


# define list A abd B
A = [1,2,3,4,5,6]
B = ([13,21,34])


# In[35]:


# concatanate A and B an define as A_B

A_B = A+B


# In[36]:


print(A_B)


# In[39]:


#create an identity matrix

np.identity(3)


# In[40]:


np.array([1,0,0], [0,1,0], [0,0,1])


# In[2]:


fuel_data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv',error_bad_lines=False)


# In[3]:


fuel_data.describe(include='all')


# In[46]:


fuel_type_code_low = fuel_data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].count()


# In[47]:


print(fuel_type_code_low)


# In[56]:


fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)


# In[49]:


print(fuel_cost_per_mmbtu_std)


# In[ ]:




