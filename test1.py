#1. Точки
#Даны N точек на плоскости (для простоты можно считать, что у всех точек целочисленные координаты). Назовём расстояние от точки A до ближайшей к ней точки B "радиусом" точки A.
#"Соседями" точки A будем называть все точки, лежащие в пределах двойного радиуса от неё включительно (кроме самой точки A).
 
#Для каждой точки из заданного набора определите её радиус и количество соседей.

#Проверка на ввод целочисленных координат точки
s = input("Введите координату Х точки: ")
try:
    x = int(s)
    print("координата подходит")
except ValueError as err:
    print(err)
s = input("Введите координату Y точки: ")
try:
    y = int(s)
    print("координата подходит")
except ValueError as err:
    print(err)
