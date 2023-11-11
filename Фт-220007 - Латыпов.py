#Создал списки для записи данных о расстоянии и тарифах
from num2words import num2words
dis = []
pri = []
summa = []
dis2 = []
pri2 = []
all_index_dis = []
all_index_pri = []
#Ввод количества сотрудников
amount = int(input('Введите количество сотрудников компании: '))
#Проверка на ошибку
while amount < 1 and  amount > 1000:
    print('Ошибка!!!')
    amount = int(input('Введите количество сотрудников компании: '))

for i in range(amount):
    distance = int(input('Введите расстояние для ' + str(i+1) + ' сотрудника: '))
    while distance < 1 and  distance > 1000:
        print('Ошибка!!!')
        distance = int(input('Введите расстояние для ' + str(i) + 'сотрудника: '))
    dis.append(distance)
    dis2.append(distance)

for j in range(0, amount):
    price = int(input('Введите тариф для ' + str(j+1) + ' такси: '))
    while price < 1 and price > 10000:
        print('Ошибка!!!')
        price = int(input('Введите тариф для ' + str(j+1) + ' такси: '))
    pri.append(price)
    pri2.append(price)

# print('Расстояние ' + str(dis))
# print('Тариф ' + str(pri))

dis2.sort()
pri2.sort(reverse = True)

for a in range(0, amount):
    itog = dis2[a] * pri2[a]
    summa.append(itog)
summa.append(sum(summa))

pri3 = pri2.copy()

for ind_dis2 in dis2:
    index_dis = dis.index(ind_dis2)
    all_index_dis.append(index_dis + 1)
for ind_pri2 in pri2:
    index_pri = pri.index(ind_pri2)
    pri[index_pri] = 0
    all_index_pri.append(index_pri + 1)

rub = ''

rub_2_to_4 = [2, 3, 4]

if summa[-1] % 100 <= 20 and summa[-1] % 100 >= 5:
    rub = ' рублей'
elif summa[-1] % 10 == 1 or summa[-1] % 100 == 1 or summa[-1] % 1000 == 1:
    rub = ' рубль'
elif summa[-1] % 10 in rub_2_to_4 or summa[-1] % 100 in rub_2_to_4 or summa[-1] % 1000 in rub_2_to_4:
    rub = ' рубля'
else:
    rub = ' рублей'

print('1. ' + str(all_index_pri))
print('2. ' + str(summa[-1]))
print('3. ' + num2words(summa[-1], lang='ru') + rub)


print('Отсортированное расстояние ' + str(dis2))
print('Отсортированный тариф ' + str(pri2))
print('Стоимость ' + str(summa))
print('Список по такси ' + str(all_index_pri))