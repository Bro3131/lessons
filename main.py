x = "123"
x = x[-1]
y = 123
z = []
f = str.join

'''
элементарные типы данных
строка str
число целочисленное int
число десятичное float
логический bool (True, False)
ничего NoneType (None)
тип данных type

составные типы:
список list
словарь dict

подробнее про список:
что это такое -- группа значений, где у каждого есть индекс начиная от 0
какие операции доступны для списков:
[1,2,3] -- конструктор списка
len(x) -- длина списка
[1,2,3][1] -- взять 1й элемент
[[1,2,3], [4,5,6], [7,8,9]][0][0] == 1
xxxxxxxxxxxx
xxxx   9xxxx
xxxx xxxxxxx
xxxx     xxx
xxxxxxxx xxx
[1, 2, 3].index(3) -- найти индекс значения
[1, 2 ,3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6] -- конкатенация(сцепление) списков
x = [1, 2 ,3]
x.append(4)
x == [1, 2, 3 ,4] -- добавить элемент в конец
y = []
# напривер, выделяем четные элементы из списка x
for a in x:
    # a = 1 шаг цикла 1
    # a = 2 шаг цикла 2
    # a = 3 шаг цикла 3
    # a = 4 шаг цикла 4
    if a % 2 == 0:
        y.append(a)
    print(a) -- выполнить чтото для всех элемсентов списка
y == [2, 4]
'''

_d = {'maxim': 'student', 4: 5, 2: 1, 0: 'abracadabra'}
# d['maxim'] == 'student' # True



# def <=> definition (определение)
# контекст использования, в разных контекстах одно и то же слово может означать разные вещи
# a + 1 = 4 <=> a = 4 - 1 <=> a = 3
def change_oil(auto_type):
    # доступиться до онлайн сервиса и узнать по типу авто какая маркировка масла нужна
    # получить ширину и долготу локации в данный момент
    # получить текущую погоду по локации
    # step 1
    # step 2
    # step 3
    ...
    # if ...:
    #       step N.1
    # else:
    #       step N.2
    # ..
    auto_with_new_oil = 1
    return auto_with_new_oil


auto = change_oil('bmw x5')


def d(key):
    if key == 2:
        return 1
    elif key == 'maxim':
        return 'student'
    elif key == 4:
        return 5
    elif key == 0:
        return 'abracadabra'

'''
_d['maxim']
d('maxim') # 'student'
d(2)
'''

def bar():
    print("hello Maxim")
    return


qwe = bar()
print(qwe)
print(type(qwe))


f1 = bar


a = input()
if a == 10:     # предикат(или условие), Буллева функция
    print('YEs')
else:
    print('NO')


def ff(arg):
    if type(arg) == list:
        pass #  сделать ничего
        pass
    else:
        print('ti debil, pereday spisor')

