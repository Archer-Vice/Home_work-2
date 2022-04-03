#### Задание 4

example_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for idx in example_list:
    answer = idx.split()[-1].capitalize()
    print("Hi, ", answer)
