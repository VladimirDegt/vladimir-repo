
##Напишите функцию, которая делает return строки приветствия людей из разных стран
##на разных языках, в зависимости от страны человека.
##Вызовите функцию используя map
##Требование: используйте map
##Для примера можете взять этот список юзеров:
##users_list = [
##    ('Александр', 'ru'),
##    ('James', 'us'),
##    ('Daniella', 'es'),
##    ('Someone', 'unknown country'),
##]
##На выходе с использованием users_list, после использования map вы должны
##получить результат iterable с такими приветствиями:
##Привет, Александр!
##Hello, James!
##Hola, Daniella!
##Hello, Someone, but I do not know where are you from!


users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
    ]
greetings_dict = {
    'ru': 'Привет, {}!',
    'us': 'Hello, {}!',
    'es': 'Hola, {}!',
    'unknown country': 'Hello, {}, but I do not know where are you from!'
}
for i in users_list 
print(*map(lambda i: greetings_dict[i[1]].format(i[0]), users_list), sep='\n')
