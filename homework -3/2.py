import collections
array = []
L = int(input('Length= '))
for i in range(L):
    N = int(input(f'N[{i}]= '))
    array.append(N)
c = collections.Counter(array)
print(max(c.most_common()))
