#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(1,len(a)-1):
        while a[i] < a[i-1] and i-1>=0:
            a[i-1],a[i] = a[i],a[i-1]
            i-=1
    return a