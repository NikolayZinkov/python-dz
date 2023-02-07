#Задание 3.
#Узнайте у пользователя целое положительное число n.
#Найдите сумму чисел n + nn + nnn.

numb = int(input("Введите целое положительное чисто n: "))
replacement = str(numb)
numb2 = replacement + replacement
numb3 = replacement + replacement + replacement
print("Сумма n+nn+nnn равна {}".format(numb + int(numb2) + int(numb3)))
