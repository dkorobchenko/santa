# -*- coding: utf-8 -*-

import os
import random
import codecs

p = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
]

bad_pairs = [
    ('Bob', 'Charlie'),
]

DEBUG_PRINT = True

######################################

def check_bad_pairs(p):
    for i in range(len(p)):
        if (p[i], p[(i+1) % len(p)]) in bad_pairs \
        or (p[(i+1) % len(p)], p[i]) in bad_pairs:
            return False
    return True

while True:
    random.shuffle(p)
    if check_bad_pairs(p):
        break

os.makedirs('result', exist_ok=True)

for i in range(len(p)):
    p1 = p[i]
    p2 = p[(i+1) % len(p)]
    fpath = os.path.join('result', p1 + '.txt')
    with codecs.open(fpath, 'w', encoding='utf8') as f:
        f.write(p2)
        if DEBUG_PRINT:
            print(p1, '->', p2)
