#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

