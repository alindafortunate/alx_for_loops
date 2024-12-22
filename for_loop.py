# A program to understand for loops.

# # List.
# fruits = ["apples", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# # Tuple.
# colors = ("red", "green", "blue")
# for color in colors:
#     print(color)

# # string
# message = "Hello, world!"
# for character in message:
#     print(character)

# # range
# for number in range(1, 6):
#     print(number)

# for number in range(4):
#     print("Attempt", number + 1, (number + 1) * ".")


# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("successful")
#         break
# else:
#     print("Tried three attempts and failed.")

# Nested loops.
# for x in range(4):
#     for y in range(4):
#         print(f"({x}, {y})")

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#         count += 1
# print(f"We have {count} even numbers")

# Challenge.

numbers = [1, 5, 3, 9]
total = 0
for number in numbers:
    total += number
print(f"The sum of the numbers is {total}.")
