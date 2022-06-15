#Напишите template строки, который можно будет многократно переиспользовать,
#вставляя в него имя и фамилию человека. Используйте метод строки "format"

while True:
    name = input("Введите имя или 0 для отмены: ")
    a = name.capitalize()
    if a == "0":
        print("Ввод закончен")
        break
    
    surname = input("Введите фамилию или 0 для отмены: ")
    b = surname.capitalize()
    if surname == "0":
        print("Ввод закончен")
        break 
              
    print("{0} {1}".format(a,b))
