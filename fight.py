import pandas as pd  #pip install openpyxl
from itertools import product
from FailPairs import failpairs
hands = [
    'прямой в голову', 'прямой в корпус', 'оверхэнд', 
    'боковой в голову', 'боковой в корпус', 'апперкот в голову', 
    'вертик. молоток вперед', 'гориз. локоть вперед', 
    'вертик. локоть вперед', 'в пах тыльн.', 'в пах ладонью', 
    'обратный молоток', 'бэкфист', 'молоток вниз', 'локоть вниз'
]

legs = [
    'регулярный', 'топчущий/проникающий вперед', 'лоу-кик', 'сайд-кик', 
    'миддл-кик', 'колено вперед', 'колено круговой', 'стоппен-кик', 'топчущий вниз',
    'хай-кик', 'вертушка'
]

side_back_h = [
    'вертик. молоток назад', 'вертик. локоть назад', 'гориз. молоток в сторону',
    'гориз локоть в сторону', 'гориз. молоток назад', 'гориз. локоть назад'
] #не больше 2х подряд

side_back_l = ['сайд-кик', 'бэк-кик'] #не больше 2х подряд

protect_h = ['скрутка', 'оттяжка', 'присед', 'сбив руки', 'блок', 'прихват', 'сбив ноги'] # какие-то +контратака одновр.

def left_right(lst):
    k1 = list(map(lambda x: x + ' ' + 'лев.', lst))
    k2 = list(map(lambda x: x + ' ' + 'прав.', lst))
    k1.extend(k2)
    return k1

hands_all = left_right(hands)
legs_all = left_right(legs)
side_back_h_all = left_right(side_back_h)
side_back_l_all = left_right(side_back_l)   #список правая-левая

hands_legs_all = hands_all.copy()   #список руки-ноги
hands_legs_all.extend(legs_all)

hands_around = hands_all.copy()   #список руки на 360
hands_around.extend(side_back_h_all)

legs_around = legs_all.copy()    #список ноги на 360
legs_around.extend(side_back_l_all)

full_around = hands_around.copy()    #список всё на 360
full_around.extend(legs_around)


n = int(input())  #количество ударов

combo_h = []
res_h = list(product(hands_all,repeat=n)) #делает список кортежей
for i in res_h:
    y = ','.join(i) #получаем строки
    if y.startswith('молоток вниз') or y.startswith('локоть вниз') or y.startswith('обратный молоток'):
        continue  #если начинается с ..., пропускаем
    elif y in failpairs:
        continue
    combo_h.append(y) #пилим из них список

h_series = pd.Series(combo_h)
h_series.to_excel('fight_h.xlsx') #версия excel нормальная должна быть, иначе закодировано


combo_l = []
res_l = list(product(legs_all,repeat=n)) #делает список кортежей
for i in res_l:
    y = ','.join(i) #получаем строки
    if y.startswith('топчущий вниз'):
        continue
    elif y in failpairs:
        continue
    combo_l.append(y) #пилим из них список

l_series = pd.Series(combo_l)
l_series.to_excel('fight_l.xlsx')

combo_h_l = []
res_h_l = list(product(hands_legs_all,repeat=n)) #делает список кортежей
for i in res_h_l:
    y = ','.join(i) #получаем строки
    if y.startswith('молоток вниз') or y.startswith('локоть вниз') or y.startswith('обратный молоток') or y.startswith('топчущий вниз'):
        continue  #если начинается с ..., пропускаем
    elif y in failpairs:
        continue
    combo_h_l.append(y) #пилим из них список

h_l_series = pd.Series(combo_h_l)
h_l_series.to_excel('fight_h_l.xlsx')


combo_h_360 = []
res_h_360 = list(product(hands_around,repeat=n)) #делает список кортежей
for i in res_h_360:
    y = ','.join(i) #получаем строки
    if y.startswith('молоток вниз') or y.startswith('локоть вниз') or y.startswith('обратный молоток'):
        continue
    elif y in failpairs:
        continue
    combo_h_360.append(y) #пилим из них список

h_ar_series = pd.Series(combo_h_360)
h_ar_series.to_excel('fight_h_360.xlsx')


combo_l_360 = []
res_l_360 = list(product(legs_around,repeat=n)) #делает список кортежей
for i in res_l_360:
    y = ','.join(i) #получаем строки
    if y.startswith('топчущий вниз'):
        continue
    elif y in failpairs:
        continue
    combo_l_360.append(y) #пилим из них список

l_ar_series = pd.Series(combo_l_360)
l_ar_series.to_excel('fight_l_360.xlsx')


combo360 = []
res360 = list(product(full_around,repeat=n)) #делает список кортежей
for i in res360:
    y = ','.join(i) #получаем строки
    if y.startswith('молоток вниз') or y.startswith('локоть вниз') or y.startswith('обратный молоток') or y.startswith('топчущий вниз'):
        continue
    elif y in failpairs:
        continue
    combo360.append(y) #пилим из них список

full_series = pd.Series(combo360)
full_series.to_excel('fight_360.xlsx')
