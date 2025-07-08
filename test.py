import random

numbers = [1, 100 , 1000]
if numbers[0] < numbers[1]:
    print("Easy")
elif numbers[2] > numbers[0]:
    print("Hard")

random_number = random.randint(numbers[0], numbers[1])


print(random_number)
