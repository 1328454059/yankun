
# coding: utf-8

# In[1]:


my_list=list(range(1,101))   
sum(my_list)


# In[2]:


sum(range(1,101))#1连加到100的算法


# In[3]:


for x in my_list:
    print(x,end='')


# In[4]:


my_list=list(range(1,10))


# In[8]:


for x in my_list:
    print('{}\t{}\t{}'.format(x,x*x,x*x*x))


# In[9]:


for row in range(1,10):
    for column in range(1,10):
        print('{}*{}={}'.format(row,column,row*column),end='\t') 


# In[13]:


for row in range(1,10):
    for column in range(1,10):
        if column>=row:
            print('{}*{}={}'.format(row,column,row*column),end='\t') 
        else:
            print('',end='\t')
print(' ')
       

