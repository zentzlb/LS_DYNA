# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:29:52 2022

@author: Logan.Zentz
"""
import numpy as np


def find(array, value, Print=False):
    
    if type(array) is list:
        array = np.array(array)
        isArray = False
    else:
        isArray = True
    
    shape = array.shape
    ndim = len(shape)
    MyList = []
    
    MyString = ''
    for i in range(ndim):
        for j in range(i):
            MyString += '\t'
        MyString += f'for ind{i} in range(shape[{i}]):\n'
    for i in range(ndim):
        MyString += '\t'
    MyString += 'if array['
    for i in range(ndim):
        if i != 0:
            MyString += f', ind{i}'
        else:
            MyString += f'ind{i}'
    MyString += '] == value:\n'
    for i in range(ndim + 1):
        MyString += '\t'
    if ndim > 1:
        MyString += 'MyList.append(['
    else:
        MyString += 'MyList.append('
    for i in range(ndim):
        if i != 0:
            MyString += f', ind{i}'
        else:
            MyString += f'ind{i}'
    if ndim > 1:
        MyString += '])'
    else:
        MyString += ')'

    if Print:
        print(MyString)
    
    exec(MyString)
    
    return MyList


    