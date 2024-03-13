number = int(input('please enter a number'))
total = 0
total_digits = 0

while number > 10:
        digit = number % 10
        total  = total + digit
        number  = number // 10
        total_digits += 1

    print('The average of all digits for ', number ,' is = ', (total/total_digits))
