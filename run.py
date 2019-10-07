#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-07
# description: file to run the program
#=================================================================================
import analysis.summer_2019
from data.pl_summer_2019 import SONGS as sg


for i in range(len(sg)):
    for k, v in sg[i].items():
        print('"{}" : {}'.format(k, v))
    print('---------------------------------------------------------')
