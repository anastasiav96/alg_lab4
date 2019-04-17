#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i+1, len(a)):
            if a[min_ind] > a[j]:
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]
    return a 