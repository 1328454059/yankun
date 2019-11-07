
# coding: utf-8

# In[3]:


for row in range(1,10):
    for column in range(1,10):
        if column>=row:
            print('{}*{}={}'.format(row,column,row*column),end='\t') 
        else:
            print('',end='\n')
print('')
       


# In[12]:


for row in range(1,10):
    for column in range(1,10):
        if column>=row:
            print('{}*{}={}'.format(row,column,row*column),end='\t') 
        else:
            print('',end='\t')
    print('')
       


# In[13]:


print('1')
print('2')

