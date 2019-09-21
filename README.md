# yankun

# coding: utf-8

# In[1]:


print('Hello,world!')


# In[8]:


a=int(input('please input a number:'))
b=int(input('please input a number:'))
print(a+b)


# In[9]:


name=input("what's your name")
print("hello,"+name)


# In[10]:


name=input("what's your name")
print("hello,{}!".format(name))


# In[11]:


a=int(input('please input a number:'))
b=int(input('please input a number:'))
print('{}+{}={}'.format(a,b,a+b))


# In[12]:


a=int(input('please input a number:'))
print('{}*{}*{}={}'.format(a,a,a,a*a*a))


# In[13]:


a=int(input('please input a number:'))
print('{0}*{0}*{0}={1}'.format(a,a*a*a))


# In[14]:


2/3


# In[15]:


2//3


# In[16]:


4%3


# In[17]:


-4%3


# In[18]:


-4//3


# In[20]:


print(hex(11),oct(11),bin(11))


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



