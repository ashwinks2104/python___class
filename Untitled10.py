#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=(1,2,3,4,5,6)


# In[7]:


a.index(6)


# In[10]:


a={1,2,3,4,5,6}
b={1,3,5,7,8,9}


# In[11]:


a.difference(b)


# In[12]:


b.difference(a)


# In[15]:


a.difference_update(b)


# In[16]:


a


# In[17]:


b.difference_update(a)


# In[18]:


b


# In[20]:


a='ASHWIN KUMAR'
a.casefold()


# In[21]:


a='aShWin KuMaR'
a.capitalize()


# In[31]:


a='ashwin2104'
a.isalnum()


# In[40]:


a='password 123'
a.isalnum()


# In[33]:


a='company123'
a.isalpha()


# In[36]:


a='projectX'
a.isalpha()


# In[37]:


a='company456'
a.isdecimal()


# In[42]:


a='123456'
a.isdecimal()


# In[54]:


a='Ashwin Kumar'
a.center(20)


# In[55]:


a='mini cooper'
a.center(50)


# In[63]:


a='!@#$%'
a.isascii()


# In[64]:


a='win !@#$'
a.isascii()


# In[69]:


a='ashwinks'
a.isidentifier()


# In[72]:


a='project@123'
a.isidentifier()


# In[ ]:




