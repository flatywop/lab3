def zad1():
    chislo = int(input("Введите число:"))
    if (chislo % 3 == 0):
     print("Число делится на 3")
    else:
     print("Ошибка")



def divide_100_by(number):
        try:
            result = 100 / number
            return result
        except ZeroDivisionError:
            print("Ошибка: на ноль делить нельзя!")
        except:
            print("Ошибка: введенное значение не является числом!")


try:
    user_number = int(input("Введите число для деления 100: "))
    print(divide_100_by(user_number))
   except ValueError:
    print("Ошибка: введено не число!")
