#Задание 2.
#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

seconds = int(input("Введите секунды: "))
print("Время в чч.мм.сс -  {}:{}:{}".format(seconds / 3600, seconds / 60, seconds))