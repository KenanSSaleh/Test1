#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd

l1=np.random.randint(1,10,20)
l2=np.random.randint(1,100,20)
l3=np.random.randint(1,10,20)
l4=np.random.randint(1,10,20)
l5=np.random.randint(1,10,20)
l6=np.random.randint(1,123,20)
l7=np.random.randint(1,10,20)
l8=np.random.randint(1,10,20)
l9=np.random.randint(1,123,20)
l10=np.random.randint(1,10,20)

#ll=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
##ll=np.array(ll)
#df=pd.DataFrame(ll)
#df

dic1= {"d1":[l1],"d2":[l2],"d3":[l3],"d4":[l4],"d5":[l5],"d6":[l6],"d7":[l7],"d8":[l8],"d9":[l9],"d10":[l10]}
df=pd.DataFrame(dic1)
df


# In[16]:


ll=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
#ll=np.array(ll)
df=pd.DataFrame(ll)
df


# In[ ]:




