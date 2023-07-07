#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 1152
s = input().split()
print(len(s))


# In[5]:


# 1371
import sys
inStr, word = sys.stdin.read(), [0 for i in range(26)]
for s in inStr:
    if s.islower():
        word[ord(s)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')

