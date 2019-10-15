#!/usr/bin python3
# -*- coding: utf-8 -*-
# 文件字符分布
# 统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果
# 同时请输出文件一共包含的字符数量
# 注意输出格式，各元素之间用英文逗号（,）分隔
# 共999字符,a:11,b:22,c:33,d:44,e:55

f = open('latex.log', 'r')
text = f.read()
count = {}
for i in range(26):
    key = chr(ord('a') + i)
    count[key] = 0

n = 0
for s in text:
    if s in count:
        count[s] += 1
        n += 1

print('共{}字符'.format(n), end='')

for x in count:
    print(',{}:{}'.format(x, count[x]), end='')
