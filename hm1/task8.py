# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).



m = int(input('Enter length of the first chocolate side: '))
n = int(input('Enter length of the second chocolate side: '))
k = int(input('How many slices do you wanna break off: '))

if m < 1 or n < 1 or k < 1:
   print('Wrong input, try again')
   exit() 

if k >= m * n: print('We dont have enough')
elif k % m == 0 or k % n == 0:  print('You can break off one')
else:  print('Sorry, but you cant do like this')