#1. Точки
#Даны N точек на плоскости (для простоты можно считать, что у всех точек целочисленные координаты). Назовём расстояние от точки A до ближайшей к ней точки B "радиусом" точки A.
#"Соседями" точки A будем называть все точки, лежащие в пределах двойного радиуса от неё включительно (кроме самой точки A).
 
#Для каждой точки из заданного набора определите её радиус и количество соседей.
import math
#заполнение списка координат точек на плоскости
def get_array_coord():
    #список координат всех точек
    arrayCoord = []
    while True:
        try:
            msg = input("Желаете ввести координату точки Y/N?")
            if (msg == "Y"):
                coord = get_coord()
                #если такая точка уже есть!
                if (coord in arrayCoord):
                    print("Данные координаты уже используются другой точкой")
                else:
                    arrayCoord.append(coord)
            elif (msg =="N"):
                #если точка одна - сообщение о необходимости ввести еще хотя бы одну точку
                if (len(arrayCoord)==1):
                    print("Введена одна точка, для выполнения задачи, необходимо ввести хотя бы еще одну")
                #если нет точек - сообщение о невозможности выполнить условия задачи
                elif (len(arrayCoord)==0):
                    print("Координаты точек не введены")
                else:
                    print ("Спасибо")
                    break
            else:
                print ("Некорректно введены данные")

        except ValueError as err:
            print (err)
    return arrayCoord
            
#Функция ввода координаты точки на плоскости
#Проверка на ввод целочисленных координат точки
def get_coord():
    s = input("Введите координату Х точки: ")
    try:
        x = int(s)
        print("координата X введена корректно")
    except ValueError as err:
        print(err)
    s = input("Введите координату Y точки: ")
    try:
        y = int(s)
        print("координата Y введена корректно")
    except ValueError as err:
        print(err)
    return (x,y)




#coord - координаты точки в кортеже (tuple)
coords = get_array_coord()
for coord in coords:
    print("Для координаты ", coord)
    i = 0
    arrayLen= []
    while i <len(coords):
        #math.hypot(x,y) - возвращает (x^2+y^2)^(1/2)
        #добавляем расстояние от точки coord до точки coords[i] в массив расстояний arrayLen
        arrayLen.append(math.hypot(coord[0]-coords[i][0],coord[1]-coords[i][1]))
        i+=1
    #Расстояние 0- расстояние от точки до точки
    arrayLen.sort()
    
    arrayLen.remove(0)
    radius = min(arrayLen)
    r2 = 2* radius
    print("Радиус = ", radius)
    countPoint2R =0
    i=0
    while arrayLen[i]<=r2:
        i+=1
        countPoint2R +=1
        if i==len(arrayLen):
            break
    print("Количество соседей = ", countPoint2R)
    
    





