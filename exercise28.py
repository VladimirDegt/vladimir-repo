##создайте файл с таким содержанием:
##"""
##    some line blablabla you dont need to catch this line try to
##    catch me but not me I'm here, catch me!!!
##"""
##откройте данный файл при помощи контекстного менеджера в режиме чтения и
##соберите список всех строк, которые содержат текст "catch me" в один список
##после чего выведите в консоль количество найденных в файле строк


with open("C:\\Users\\Владимир\\Desktop\\exercise28.txt", "w", encoding="utf-8" ) as file:
    file.write("some line blablabla you dont need to catch this line try to catch me but not me I'm here, catch me!!!")
with open("C:\\Users\\Владимир\\Desktop\\exercise28.txt", "r") as file:
    str_ = file.read()
    word = str_.split()
s = "".join(word)
a = s.count("catchme")
l=[]
for i in range(a):
    l.append("catch me")
print(a)
print(l)


    



