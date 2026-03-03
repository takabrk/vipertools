#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
loto_random.py
"""
import random

loto7 = [1,2,6,7,9,10,12,13,14,17,20,22,24,29,30,33,34,35,37]
loto6 = [1,2,5,6,7,10,12,14,15,16,17,21,22,24,25,26,27,28,29,30,33,35,38,39,41,42]
miniloto = [3,4,6,11,12,13,16,20,21,22,25,27,28,29,31]

print("ロト7の買い目は、",sorted(random.sample(loto7,7)))
print("ロト6の買い目は、",sorted(random.sample(loto6,6)))
print("ミニロトの買い目は、",sorted(random.sample(miniloto,5)))

