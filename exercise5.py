#Дана строка из имён, в формате "Денис, Олег, Вася, Петя,Дима,Женя".
#Разбейте строку так, чтобы получился список имён.
#Заметьте: после запятой не всегда есть пробел
#(он не должен входить в имена, которые попадут в список)


names = "Денис, Олег, Вася, Петя,Дима,Женя"

lst = names.split(", ")
lst2 = lst[3]
lst3 = lst2.split(",")

print(lst[:3] + lst3)

