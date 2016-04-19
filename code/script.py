#!/usr/bin/python -tt

import sys
import os

from collections import *


def main():
    if  len(sys.argv) != 4:
        print 'usage: {} <FILE1> <FILE2> <OUT>'.format(sys.argv[0])
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    out = sys.argv[3]

    print "file1 = {}".format(file1)

    f1 = open(file1,'r')
    f2 = open(file2,'r')
    o = open(out,'w+')

    reviews1 = {}
    reviews2 = {}
    for l in f1.readlines():
        rating = l.strip()[-1:]
        user = l.strip().split('-')[0].strip()
        restaurant = l.strip().split('-')[1][:-1].strip()

        reviews1[restaurant] = reviews1.get(restaurant,0)




        print '{} -- {} -- {}'.format(user, restaurant, rating)        


    


if __name__ == '__main__':
    main()


