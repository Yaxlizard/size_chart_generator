# -*- encoding: utf8 -*-
import re

'''
一个自动把厘米尺码换算成英寸尺码的脚本，转换后生成一个尺码表
'''

class Customize:
    def __call__(self):
        ls = []
        print self.welcome
        str = raw_input('devide with space: ')
        str = str.strip()
        ls = str.split() #默认为空格
        return ls

class setSize(Customize):
    def __init__(self):
        self.welcome = 'customize your size'

class setPart(Customize):
    def __init__(self):
        self.welcome = 'customize different parts'

def function(value,part):
    str_value = value
    value = float(value)
    trs_value = value/2.54
    trs = ' %s %scm(%0.2f")' %(part,str_value,trs_value)
    return trs

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            output = func(*args, **kw)
            print text
            return output
        return wrapper
    return decorator

#带@的装饰器引用的参数必须写在前面！
text = 'Attention !!!: This item is of Asian size as above, and the size deviates from the offical size chart below.'

@log(text)
def output(size_ls,part_ls):
    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            pass
    #如果不想传参也想使用外面的变量，就得把外面的全局化
    output = ''
    for size in size_ls:
        record = []
        print '\nCurrently editting size %s...' %size
        for part in part_ls:
            #循环判断字符串内容是否为数字（整数或小数），若是则跳出循环
            while True:
                print 'Please input %s: ' %part,
                value = raw_input().strip()
                if is_number(value):
                    break
                print 'Not the correct value !\n'
            trs = function(value,part)
            record.append(trs)
        row = size +':' + ','.join(record) + '\n'
        output = output + row
    print output
    
s = setSize()
p = setPart()
while True:
    size_ls = s()   #调用__call__
    part_ls = p()
    output(size_ls,part_ls)
