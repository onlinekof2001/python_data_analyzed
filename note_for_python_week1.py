# -*- coding: utf-8 -*-
import sys
import os
print("Hello world!")
print 'Hello world!'

"""代码组"""
if True:
    print "True"
elif True:
    print "True"
else:
    print "False"


""" \ 连接符"""
item1 = 1
item2 = 2
item3 = 3
total_items = item1 + \
item2 + \
item3
print total_items

'''空行'''
#raw_input("\n\nPress the enter key to exit.")

x = 'Hello sys model'
sys.stdout.write(x + '\n')

'''变量赋值'''
counter = 100
kilometer = 10
time = 60
miles = 19.5
name = 'John'

'''删除对象引用'''
#del counter

'''字符串的切片'''
start = 'First learning Python'
print start[1:5]
print start[5:-1]   # -1 is len()-1
print start[2:5] * 2 + "Peer"  # 2nd to 4th letters shows twist and plus a word

'''列表'''
list = ['Male', 7123, 123, 4123.2, 'John']
tinylst = ['Female', 155]


print list[0]
print list[0:3] + tinylst * 2
list[2] = 321
print list


'''元祖'''
tuple = ('Male', 7123, 123, 4123.2, 'John')
tinytpl = ('Female', 155)

print tuple[0]
print "I'm tuple", tuple[0:3] + tinytpl * 2

# tuple[2] = 321 is not support for tuple.
print tuple

'''元字典'''
dict = {}
dict['one'] = "first"
dict[2] = 'second'
tinydict = {'name': 'John', 'Code': 6513, 'dept': 'Admin' }

print tinydict['name'], dict[2], tinydict.keys(), tinydict.values()

'''运算'''
print "", counter/kilometer
print "plus is", counter + kilometer
print counter - miles

print "mod is ", miles % kilometer
print "int is ", miles // kilometer

"""比较"""
print counter == kilometer
print counter != kilometer
print counter <> kilometer
print counter > kilometer
print counter >= kilometer

'''赋值运算'''
a = 2
counter += 1
print counter
miles -= 1
print miles
kilometer *= 2
print kilometer
kilometer /= 2
print kilometer
counter %= 2
print counter
a **= 2
print a

print id(a)


