# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from enum import Enum



class cls_test:
    def __init__(self, aa, bb, cc, dd):
        self.enmA = aa
        self.enmB = bb
        self.enmC = cc
        self.enmD = dd
    

aryData = {'00': '一',
           '11': '二'}

TT =cls_test('a',200,300,400)

print(TT.enmA)
