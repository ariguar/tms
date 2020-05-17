array = []
for i in range(5):
    N = int(input(f'N[{i}]= '))
    array.append(N)
x = int(input('x = '))
if x in array:
    print('Index is', array.index(x))
else:
    print('NOT')
