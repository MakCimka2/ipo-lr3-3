a = int(input("Введите дату: ")) #Запрашиваем дату
b = int(input("Введите месяц: ")) #Запрашиваем месяц

if a <= 0 or b <= 0: # Проверяем верно ли введены числа
    print("Неверные значения") # Выводим неверное значение
elif (a >= 1 and a <= 30 and b == 9) or (a >= 1 and a <= 31 and b == 10) or (a >= 1 and a <= 30 and b == 11): #Проверяем подходят ли значениря для Осени
    print("Осень") #Выводим осень
elif (a >= 1 and a <= 31 and b == 12) or (a >= 1 and a <= 31 and b == 1) or (a >= 1 and a <= 28 and b == 2): #Проверяем подходят ли значениря для Зимы
    print("Зима") #Выводим Зиму
elif (a >= 1 and a <= 31 and b == 3) or (a >= 1 and a <= 30 and b == 4) or (a >= 1 and a <= 31 and b == 5): #Проверяем подходят ли значениря для Весны
    print("Весна") #Выводим Весну
elif (a >= 1 and a <= 30 and b == 6) or (a >= 1 and a <= 31 and b == 7) or (a >= 1 and a <= 31 and b == 8): #Проверяем подходят ли значениря для Лета
    print("Лето")  # Выводим Лето
else: #Если ни одно из условий выше не подошло, то
    print("Неверная дата") # Выводим неверную дату
