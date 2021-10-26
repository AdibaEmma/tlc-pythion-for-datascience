# # Q1.
# world = input("enter string")
# print(f"Hello {world}")
#
# # Q2
# number = int(input("Enter a number"))
#
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#

# # Q3.
# name = "Emma"
# age = 22
# print(name)
# print(age)
#
# print(f"{name} is {age} years old")

# Q4.
# import random
#
# end_range = 20
# random_number = random.randint(1, end_range)
# print(random_number)
# while True:
#     number = input("Guess the number from 1 to 20 (enter e to exit): ")
#     if number[0] != 'e':
#         if int(number) == random_number:
#             print("You guessed right")
#             continue_game = input("press c to continue the game, e to exit")
#             if continue_game[0] == "c":
#                 continue
#             else:
#                 break
#         else:
#             print(f"Guess again")
#     elif not number <= end_range:
#         print("Oops, you are out of range")
#     else:
#         print("bye\nCome again some time")
#         break

# Q5.
# my_list = [1, 4, 9, 16, 25]
# my_tuple = (1, 4, 9, 16, 25)
#
# for number in my_list:
#     if number % 2 == 0:
#         print(number)


# Q6.
age = int(input("enter age: "))
years_list = list(range(1, age + 1))
years_in_value = 0
for num in years_list:
    years_in_value += num
print(f"Total age value in years is {years_in_value}")
print(f"Total age value in months is {years_in_value * 12}")
print(f"Total age value in days is{years_in_value * 365}")
print(f"Total age value in hours is {years_in_value * 365 * 24}")

