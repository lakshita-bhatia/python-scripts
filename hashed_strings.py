# The function hash_string,
# takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    k = []
    s = 0
    k.extend(keyword)
    for i in k:
        s += ord(i)
    s = s%buckets
    return s




print hash_string('a',12)
#>>> 1

#print hash_string('b',12)
#>>> 2

#print hash_string('a',13)
#>>> 6

#print hash_string('au',12)
#>>> 10

#print hash_string('udacity',12)
#>>> 11
