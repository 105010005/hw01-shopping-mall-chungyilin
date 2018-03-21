
# coding: utf-8

# In[ ]:


Type=list(input('Please type anything\n'))
Set=set(Type)
for elements in Set:
    dictionary={elements :Type.count(elements)}
    for item in dictionary.items():
        letters,numbers=item
        print(letters,numbers,sep=':')
input()

