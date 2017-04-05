__author__ = 'JMYoung'
from random import randrange


for listSize in range(1000,10001,1000):
    alist = [randrange(10) for x in range (listSize)]
    print(alist)