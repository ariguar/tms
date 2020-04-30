first_list = []
second_list = []
x = 0
N = int(input('Enter number N (n>2): '))
for number in range(N):
    first_list.append(int(input('Enter number from this list: ')))
print(f"First list: {first_list}")
for number in first_list:
    if number == x:
        second_list.insert(0, number)
    if number != x:
        second_list.append(number)
print(f"\nYour right list is: {second_list}  Congratulations!")
