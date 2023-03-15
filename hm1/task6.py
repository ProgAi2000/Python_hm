# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет "счастливость" билета.

def ticketnumber():
    while (number := input('Enter ticket number: ')).isdigit() == False or (100000 <= int(number) < 1000000) == False:
        print('Wrong input ticket number (the number must be have of 6 digits), try again')
    return int(number)

def sumOfDigits(number):
    count = 0
    while number != 0:
        count += number % 10
        number //= 10
    return count

number = ticketnumber()
sumOfFirst3Digits = sumOfDigits(number // 1000)
sumOfLast3Digits = sumOfDigits(number % 1000)

if sumOfFirst3Digits == sumOfLast3Digits:
    print('You have a lucky ticket!')
else:
    print('Your ticket is not lucky :(')
