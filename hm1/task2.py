# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Enter 3-digit number: '))

if number < 100 or number > 999:
    print ('Wrong input number, try again ')
    exit()

def sumOfDigits(number):
    count = 0
    while number != 0:
        count += number % 10
        number //= 10
    return count

result = sumOfDigits(number)
print('Sum of digits of', number, 'equal to', result)