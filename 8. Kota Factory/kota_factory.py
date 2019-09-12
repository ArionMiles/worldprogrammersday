import math
from collections import defaultdict
from functools import reduce

def make_grps(dummies, n):
    l = []
    i_range = 2**n - 1
    for i in range(1, i_range):
        g = defaultdict(list)
        for j in range(n):
            if i & (1 << j):
                g["G1"].append(dummies[j])
            else:
                g["G2"].append(dummies[j])
        l.append(g)
    return l

def calc_gcd(grps):
    gcd_is_one = 0
    for grp in grps:
        if len(grp['G1']) == 1:
            e1 = grp['G1'][0]  
        else:
            e1 = reduce((lambda x, y: x*y),  grp['G1'])
        
        if len(grp['G2']) == 1:
            e2 = grp['G2'][0]
        else:
            e2 = reduce((lambda x, y: x*y),  grp['G2'])

        if math.gcd(e1, e2) == 1:
            gcd_is_one += 1
    print(gcd_is_one)


if __name__ == '__main__':
    n = 4 # int(input())
    dummies = [2, 3, 5, 10] #list(map(int, input().split()))
    grps = make_grps(dummies, n)
    calc_gcd(grps)
