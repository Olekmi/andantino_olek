from collections import Counter
import numpy as np

def intersection (seq):
    res=[seq[i] for i in range(len(seq)) if seq[i] in seq[:i]][1:]
    return res

def intersection2 (seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    hexes_neigh = list(set( x for x in seq if x in seen or seen_add(x) ))
    return hexes_neigh 

def intersection3(seq):
    seq = np.array(seq)
    temp = [item for item, count in Counter(seq).items() if count > 1]
    return temp

def intersection4(seq):
    a = []
    for i in range(len(seq)):
        for j in range(len(seq)):
            if seq[i]==seq[j] and i!=j and seq[i] not in a:
                a.append(seq[i])
    return a


a = np.array([1, 2, 1, 3, 3, 3, 0])
test = [1,2,1,4,5,7,7,7,8]
print(intersection(test))
out = intersection3(test)
print(out)
print(intersection4(test))

ar1 = [1,2,3,4]
ar2 = [1,1,1,1]
print(ar1+ar2)