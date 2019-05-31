# -*- coding：utf-8 -*-
# print("hello world")
# print(ord('A'))
import re

# print("case1")
# f = open('C:/Users/STUYID/Desktop/2.txt','r')
# result = list()
# for line in f.readlines():
#     # print(line)
#     line = line.strip()
#     result.append(line)
# print(result)
# f.close()                
# open('C:/Users/STUYID/Desktop/result.txt', 'w').write('%s' % '\n'.join(result))

print("case2")
f = open('C:/Users/STUYID/Desktop/1.txt','r')
result = list()
for line in f.readlines():
    line = line.strip()
    l = re.findall('.*title =        "(.*)"',line)
    if len(l):
        # print(l)
        l = "".join(l)
        msg ='title =        "{%s}",' %l
        result.append(msg)
    else:
        result.append(line)
# print(result)
f.close()                
open('C:/Users/STUYID/Desktop/result.txt', 'w').write('%s' % '\n'.join(result))