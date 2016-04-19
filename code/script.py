#!/usr/bin/python -tt

import sys
import os
from collections import defaultdict
from collections import *
from numpy import mean


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
    reviews1 = defaultdict(list)
    reviews2 = defaultdict(list)
    for l in f1.readlines():
        rating = int(l.strip()[-1:])
        user = l.strip().split('-')[0].strip()
        restaurant = l.strip().split('-')[1][:-1].strip().lower()
        reviews1[restaurant].append(rating)
    f1.close()

    for l in f2.readlines():
        rating = int(l.strip()[-1:])
        user = l.strip().split('-')[0].strip()
        restaurant = l.strip().split('-')[1][:-1].strip().lower()
        reviews2[restaurant].append(rating)
    f2.close()

    # Merging file data
    review1_keys = set(reviews1.keys())
    review2_keys = set(reviews2.keys())

    temp_reviews = {}
    merge_reviews = reviews1.copy()
    common_keys = list(review1_keys & review2_keys)
    for k in common_keys:
        temp_reviews[k] = reviews1[k] + reviews2[k]

    merge_reviews.update(reviews2)
    merge_reviews.update(temp_reviews)

    for restaurant, ratings in merge_reviews.iteritems():
        o.write(restaurant + ' ' + str(mean(ratings)) + '\n')
    o.close()

if __name__ == '__main__':
    main()


