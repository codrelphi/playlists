#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-05
# description: basic analysis on my playlist of the summer 2019
#              basic analysis done just for fun.
#=================================================================================
from data_playlist_summer_2019 import SONGS

for k, v in SONGS[0].items():
    print('"{}" : {}'.format(k, v))
