#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#0,1,1,2,3,5,8
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
print(fib(6))