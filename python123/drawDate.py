#!/usr/bin python3
# -*- coding: utf-8 -*-

import turtle as t
import time

def drawGap():
    t.penup()
    t.fd(5)

def drawLine(flag):
    drawGap()
    t.pendown() if flag else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

def drawDigit(d):
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    t.left(90)

    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180)

    t.penup()
    t.fd(20)

def drawDate(date):
    t.pencolor('red')
    for i in date:
        drawDigit(eval(i))

def main():
    t.setup(800, 600)
    t.pensize(2)
    t.penup()
    t.fd(-300)
    date = time.strftime('%Y%m%d', time.gmtime())
    print(date);
    drawDate(date)
    t.done()

if __name__ == '__main__':
    main()