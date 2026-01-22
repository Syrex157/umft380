from proekt380Kamilov import MinNumber

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

check = MinNumber(a, b, c)
print("Наименьшее число:", check.find_min())



from project380TursunovJavoxir import NumberType

num = int(input("Введите число: "))
check = NumberType(num)
print(check.result())