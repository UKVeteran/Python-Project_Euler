# -*- coding: utf-8 -*-
"""ProjEulerProb4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ba97SjiQJ8RfMiFdNJM8J98UotYnOZyq
"""

n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b

print (n)