numbers = []
N = int(input('Enter number N (n>2): '))
for number in range(N):
    numbers.append(int(input('Enter number from this list: ')))
numbers.sort()
print('\nTwo biggest numbers are', numbers[-2:])




