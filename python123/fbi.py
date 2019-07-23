#!/usr/bin python3
# -*- coding: utf-8 -*-
# 斐波那契数列计算

def fbi(n):
    if n == 1 or n == 2:
        return 1

    return fbi(n-1) + fbi(n-2)

n = eval(input())
print(fbi(n))