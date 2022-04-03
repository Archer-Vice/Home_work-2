#### Задание 5

price_list = [56.91, 45.12, 432.34, 98.09, 100, 65, 21, 457, 346.7, 45.87, 32.56, 71.20, 80.23, 15.94, 89.78]

for price in price_list:
    price = int(round(price * 100))
    rub = price // 100
    kop = price % 100
    print(f'{rub:02d} руб {kop:02} коп', end = ", ")
print(id(price_list))
print("--------->")

price_list.sort()
for price in price_list:
    price = int(round(price * 100))
    rub = price // 100
    kop = price % 100
    print(f'{rub:02d} руб {kop:02} коп', end = ", ")
print(id(price_list))
print("-------->")

price_rev = sorted(price_list, reverse=True)
for price in price_rev:
    price = int(round(price * 100))
    rub = price // 100
    kop = price % 100
    print(f'{rub:02d} руб {kop:02} коп', end = ", ")

print(id(price_rev))