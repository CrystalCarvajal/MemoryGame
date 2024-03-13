number = int(input("please enter a number"))
total = 0

while number > 0:
    digit = number % 10
    total = number + digit
    number = number // 10

print("the sum of all digits for", number , is = , total)
