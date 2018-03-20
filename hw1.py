
# coding: utf-8

# In[49]:


print('We have 1.PS4 Pro  2.Nintendo switch   3.Xbox one x')


# In[50]:


print('')


# In[51]:


a=['empty','"PS4 Pro"','"Nintendo switch"','"Xbox one X"']


# In[52]:


b=[0,10000,9000,15000]


# In[53]:


c=int(input('Which one do you want to buy?[1,2,3]'))


# In[54]:


d=a[c]


# In[55]:


e=int(input('How many '+ d +' do you want to buy?'))


# In[56]:


f=int(input('How much money do you have?'))


# In[57]:


g=b[c]


# In[58]:


h=g*e


# In[59]:


print("-------------------")


# In[60]:


print('You want to spend '+str(h)+' dollars to buy '+str(e),d+'.')


# In[61]:


i=f>=h


# In[62]:


print('Do you have enough money?',i) 


# In[63]:


if i is True:
    print('Congratulations!you can buy '+str(e),d+'.','\nAnd you will have '+str(f-h)+' left.')
else:
    print('But actually you can buy '+str(f//g),d+'.','\nThen,you will have '+str(f%g)+' left.')



# In[64]:


input()

