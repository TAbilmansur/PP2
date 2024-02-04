import itertools as it
k = dict()
def permutations_of_a_string(a):
    for p in it.permutations(a):
        if (k.get(p)):
            continue
        k[p] = True
        for i in p :
            print(i,end = '')
        print()
a = input()
permutations_of_a_string(a)