print ("Приветствуем вас в калькуляторе Python!")
q1 = int (input("Введите число 1: "))
q2 = int (input("Введите число 2: "))

try:
    v = int (input ("Какую операцию вы хотите выполнить? \n 1 - Сложение \n 2 - Вычитание \n 3 - Деление \n 4 - Умножение \n"))
except(ValueError):
    print("Ошибка! Пожалуйста, введите число.\n ")
    v = int (input ("Какую операцию вы хотите выполнить? \n 1 - Сложение \n 2 - Вычитание \n 3 - Деление \n 4 - Умножение"))
    
if v == 1:
       r = q1 + q2
       p = "сложения"
       t = p

if v == 2:
       r = q1 - q2
       l = "вычитания"
       t = 1

if v == 3:
       r = float(q1 / q2)
       m = "деления"
       t = m

if v == 4:
       r = q1 * q2
       n = "умножения"
       t = n
print("Рузультат ", t, " - ", r)
