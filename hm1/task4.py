# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def sumofallcranes():
  while (sum := input('Enter amount of paper cranes: ')).isdigit() == False or (int(sum) % 6 == 0) == False:
        print('Wrong input (the amount must be a multiple of 6), please try again')
  return int(sum)

result = sumofallcranes()

resultPeter = result // 6
resultSerj = result // 6
resultKate = result // 3 * 2 

print('Peter made', resultPeter, 'of the paper cranes')
print('Katy made', resultKate, 'of the paper cranes')
print('Sergei made', resultSerj, 'of the paper cranes')