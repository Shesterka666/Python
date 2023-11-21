import numpy as np
print(np.__version__ )
np.zeros((10))
z = np.zeros((10))
print(z.itemsize*z.size)
x = np.arange(10,50)
print(np.flip(x))
print(np.arange(9).reshape(3,3))
#1 Создайте случайный вектор размером 30 и найдите среднее значение
vec = np.random.random(30)
print(vec.mean())
#2 Создайте двумерный-массив с 1(единицами) на границе и 0(нулями) внутри
z = np.ones((4,4))
z[1:-1,1:-1] = 0
print(z)
#3 Как добавить границу (заполненную нулями) вокруг существующего массива (например: массив 5 на 5 из единиц окружить нулями, чтобы он превратился в массив 7 на 7?
x = np.ones((5,5))
x = np.pad(x, pad_width=2, mode='constant', constant_values=0)
print(x)
#4 Создайте матрицу 5 на 5 со значениями 1,2,3,4 сразу ниже диагонали
print(np.diag(np.arange(1,5),k=-1))
#5 Создайте матрицу 8x8 и залейте ее шахматным узором Пояснение к заданию: не используйте функцию tile. Ниже будет аналогичное задание 21 с использованием функции tile
x = np.zeros((8,8),dtype=int)
x[0::2,1::2] = 1 #первые строки нечет
x[1::2,0::2] = 1
print(x)
#6 Создайте матрицу шахматной доски 8x8, используя функцию tile
array= np.array([[0,1], [1,0]])
z = np.tile(array,(4,4))
print (z)
#7 Рассмотрим массив формы (6,7,8), каков индекс (x, y, z) 100-го элемента
print(np.unravel_index(indices=99,shape=(6,7,8))) #сотый же имеет индекс 99
#8 Нормализовать матрицу случайных значений 5 на 5
z = np.random.random((5,5))
max, min = z.max(), z.min()
z= (z-min)/(max-min)
print(z)
#9 Создайте настраиваемый dtype, который описывает цвет как четыре байта без знака (RGBA)
color = np.dtype([("R", np.ubyte, 1),("G", np.ubyte, 1),("B", np.ubyte, 1),("A", np.ubyte, 1)])
#10 Умножьте матрицу 5x3 на матрицу 3x2 (матричное произведение)
a = np.random.randint(7, size=(2,2))
b = np.random.randint(7, size=(2,2))
print(a)
print(b)
print(a @ b)
print(b @ a)
# 11 задан одномерный массив, инвертируйте (поменяйте знак) у всех элементов массива, которые находятся в диапазоне от 3 до 8, прямо в нем самом (без перезаписывания значений).
z = np.arange(11)
z[(3 < z) & (8 > z)] *= -1
# 12 что выведет следующий скрипт?
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
# 13 Каковы результаты следующих выражений?
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
# 14 Как округлить Вверх массив с плавающей запятой?
z = np.random.uniform(-10,+10,10)
print(np.copysign(np.ceil(np.abs(z)), z))
print(np.trunc(z + np.copysign(0.5,z)))
# 15 Как найти общие значения между двумя массивами
z1 = np.random.randint(0,10,10)
z2 = np.random.randint(0,10,10)
print(np.intersect1d(z1,z2))
# 16 Как игнорировать все предупреждения о numpy
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
_ = np.seterr(**defaults)
with np.errstate(all="ignore"):
    np.arange(3) / 0
    #нашел в инете 
# 17Верно ли следующее выражение?
print(np.sqrt(-1) == np.emath.sqrt(-1))
# 18 Как получить даты вчера, сегодня и завтра
yesterday = np.datetime64('today') - np.timedelta64(1)
today = np.datetime64('today')
tomorrow  = np.datetime64('today') + np.timedelta64(1)
# 19 Как получить все даты, соответствующие июлю месяцу 2016
z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(z)
# 20 Как вычислить ((A + B) * (- A / 2)) на месте (без копирования - то есть без создания дополнительного массива кроме существующих A, B)?
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
# 21 Извлеките целую часть случайного массива положительных чисел, используя 4 разных метода.
Z = np.random.uniform(0,10,10)
print(Z - Z%1)
print(Z // 1)
print(np.floor(Z))
print(Z.astype(int))
print(np.trunc(Z))
# 22 Рассмотрим функцию генератора, которая генерирует 10 целых чисел и использует ее для построения массива.
def generate():
    for x in range(10):
        yield x
print(np.fromiter(generate(),dtype = float,count = -1))
# 23 Создайте вектор размера 10 со значениями от 0 до 1, за исключением границ отрезка 0 и 1.
z = np.linspace(0,1,11,endpoint=False)[1:]
print(z)
# 24 Рассматривая матрицу 10x3, извлеките строки с неравными значениями (например, [2,2,3])
nums = np.random.randint(0,4,(6,3))
print(nums)
new_nums = np.logical_and.reduce(nums[:,1:] == nums[:,:-1], axis=1)
result = nums[~new_nums]
print(result)
# 25 Как получить суммы по двум последним осям заданного четырехмерного массива ?
z = np.random.randint(0,10,(3,4,3,4))
sum = z.sum(axis=(-2,-1))
print(sum)
sum = z.reshape(z.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
# How to get the diagonal of a dot product? 
A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))
np.diag(np.dot(A, B))
np.sum(A * B.T, axis=1)
np.einsum("ij,ji->i", A, B)