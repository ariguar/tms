import random

x = random.randint(1, 11)
print(f"secret number is {x}")
while True:
    number = int(input('\nEnter your number: '))
    if number == x:
        print('Yar are right!')
        break
