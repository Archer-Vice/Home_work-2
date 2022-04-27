### Задание 1.
""" 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration... """

def odd_nums (nums):
    for i in range (1, nums + 1):
        if i % 2 != 0:
            yield (i)


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))


### Задание 2.
""" 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield. """

""" Временная версия - 1 """

f = (i for i in range(1, int(input("number: ")) + 1) if i % 2 != 0)

print(next(f))
print(next(f))
print(next(f))


""" Конечная версия - 2 """

def odd_nums (nums):
    f = (i for i in range(1, nums + 1) if i % 2 != 0)
    return f

odd_to_10 = odd_nums(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))

### Задание 3.
""" 3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
генератор даст эффект. 

### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

Подсказка: использовать возможности python, изученные на уроке. """

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А'] #, '10Б', '9А']

### Not full version 1

def gen_tut_klas (tutors, klasses):
    for i in range(len(tutors)):
        yield (tutors[i], klasses[i])
        if klasses[i] == 0:
            yield (tutors[i], None)


gen_tut_klas(tutors,klasses)


a = gen_tut_klas(tutors, klasses)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


""" Версия 2 (к сожалению, пока не понял, как прописать код, чтобы чтобы цикл продолжался, когда лист закончился. 
Поэтому пришлось гуглить и искать другие варианты решения вопроса) """

from itertools import zip_longest

iterator = zip_longest(tutors, klasses[:len(tutors)])
print(list(iterator))


"""4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

def my_nums_gen(my_rand_list):
    for i in range(len(my_rand_list)):
        if my_rand_list[i] < my_rand_list[i + 1]:
            yield (my_rand_list[i+1])
        elif my_rand_list[i + 1] > len(my_rand_list):
            break


x = my_nums_gen(src)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


""" 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание. """

### Вариант 1
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

y = []

for i in src:
    if src.count(i) == 1:
        y.append(i)

print(y)


### Вариант 2

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

y = (i for i in src if src.count(i) == 1)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))