#!/usr/bin python3
# -*- coding: utf-8 -*-
# 汉诺塔实践
# 首先将 n-1 从 A 移动到 B
# 然后将 n   从 A 移动到 C
# 最后将 n-1 从 B 移动到 C

steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps += 1
        print('[Step{:>4}] {}->{}'.format(steps, src, des))
    else:
        hanoi(src, mid, des, n-1)
        steps += 1
        print('[Step{:>4}] {}->{}'.format(steps, src, des))
        hanoi(mid, des, src, n-1)

n = eval(input())
hanoi('A', 'C', 'B', n)
