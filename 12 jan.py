#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[5]:


arr=np.arange(100)
arr


# In[6]:


arr.reshape(10,10)


# In[7]:


x= [[2,3,4], [6,7,8], [5,4,3]]
ar=np.array(x)
ar


# In[8]:


ar.sum(axis=0)
# axis0 is addition of each row


# In[9]:


ar.sum(axis=1)
#axis 1 is addition of each col


# In[10]:


ar.T
# row converted to col


# In[12]:


arr1=np.arange(20)
arr1


# In[13]:


arr1+arr1


# In[14]:


arr2=arr1


# In[15]:


arr2[:10]


# In[16]:


arr3=arr2


# In[17]:


arr3[:10]=80


# In[18]:


arr3


# In[19]:


import numpy as np


# In[20]:


arr=np.arange(0,20)


# In[21]:


arr


# In[22]:


arr=np.arange(10,100,5)


# In[23]:


arr


# In[24]:


arr[-1]


# In[25]:


arr[9]


# In[26]:


arr[1:11:3]


# In[27]:


arr=np.array([2,4,56,788,900,3325,909,45])
arr


# In[28]:


arr<500


# In[29]:


arr>800


# In[30]:


len(arr)


# In[31]:


np.where(arr<200)


# In[32]:


np.where(arr>400)


# In[34]:


arr_2d=np.array(([2,3,4],[6,7,8],[3,9,7]))
arr_2d


# In[35]:


arr_2d[1:4]


# In[36]:


arr_2d[1:,:2]


# In[ ]:




