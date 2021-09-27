# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:12:09 2021

@author: souhe
"""


import numpy as np
import matplotlib.pyplot as plt
import json

TS = '''
{
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": true,
"droppedStudents": null,
"date": 20210927,
"data": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}
'''

datab = json.loads(TS)
data = datab.get("data")
L = len(data)
for i in range(L):
    x = data[i][0]
    y = data[i][1]
    plt.plot(y,x, '.b')

plt.title(datab.get("courseName"))
    
