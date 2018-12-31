#!/usr/bin/env python
# coding: utf-8

# In[14]:


##############################################
# A function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n
def filter_long_words(lst,length):
    newlst = []
    for x in range(len(lst)):
        if len(lst[x]) > length:
            newlst.append(lst[x])
        
    return newlst

#############################################

lst = ['Sam', 'John', 'Steve']
n = 3
print("Below is the new List of words that are longer than length %s " %(n))
print(filter_long_words(lst,n))

