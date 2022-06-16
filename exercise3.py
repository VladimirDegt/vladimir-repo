# Дан список из строк. Создайте однострочное решение
#(при помощи list comprehension), которое приведёт к верхнему регистру
#все строки, содержащие слово 'price')

##lst = "pricered", "price", "red"
##for i in lst:
##    if "price" in i:
##        i = i.upper()
##    else:
##        i = i
##    print(i)


lst = ("price", "34", "red", "pricered")
print([i.upper() if "price" in i else i for i in lst ]) 


  
