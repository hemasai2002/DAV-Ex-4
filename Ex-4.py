#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[11,22,33,44]])
print('First Array:')
print(a)


# In[4]:


print('The shape of first array:')
print(a.shape)


# In[7]:


b = np.resize(a,(5,2))
print(b)


# In[8]:


print('The shape of Second Array:')
print(b.shape)


# In[10]:


print('Resize the second array:')
c = np.resize(b,(3,3))
print(c)


# In[ ]:




