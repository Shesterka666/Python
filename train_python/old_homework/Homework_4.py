#import typing 
from typing import Union

#Шахматный «обед»
def can_eat(horse: tuple, figura:tuple)-> bool:
    #проверки на поле не будет (на корректность данных)
    #фишка в том , что разница между коордиатами всегда будет 2.1 1.2 -1.2 и тд
    # т.е abs(x*y)=2
    task = abs(horse[0]-figura[0])*abs(horse[1]-figura[1])
    return task == 2

def task_resheto(Buuf: int) -> bool:
    for j in range(2, Buuf):
        if Buuf % j == 0:
            return False #непростое 
    return True #простое

#Напишите функцию is_prime, которая принимает натуральное число, а возвращает 
#булево значение: True — если переданное число простое, а иначе — False
def is_prime(natural: int)-> bool:
    return task_resheto(natural)

#Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
#Параметры функции:
#size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы); value — значение элементов списка (по-умолчанию 0).
##Переделать!!!!
def make_matrix(size: tuple, x = 0):
    a = []
    if isinstance(size,int): return [[x for _ in range(size)] for _ in range(size)]
    else:
        for i in range(size[0]):
            aa = []
            for j in range(size[1]):
                aa.append(x)
            a.append(aa)
        return a

def matr_cheak(n,x):
    a = make_matrix(n,x)
    for i in range(n):  
        for j in range(n):  
            print(a[i][j], end = " ")  
        print() 

def get_average():
    pass

def task_5():
    fuc = lambda x: (len(x), x.lower())
    string = 'мама мыла раму и пару рублей яблок и салоет силает сялоет'
    print(sorted(string.split(), key= lambda x: (len(x),x.lower())))

def recursive_digit_sum(n: int): 
    if n < 10:
        return n
    return recursive_digit_sum(n // 10) + n % 10

def merge_sort(s):# Сортировка списка рекурсивная
    if len(s) ==1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left,right)

def merge_two_list(l, r):
    buuf =[]
    i = j = 0
    while i<len(l) and j < len(r):
        if l[i]<r[j]:
            buuf.append(l[i])
            i+=1
        else: 
            buuf.append(r[j])
            j+=1
    if i < len(l):
        buuf += l[i:]
    if j < len(r):
        buuf += r[j:]
    return buuf

def make_linear(glist): 
    res = [] 
    for subglist in glist: 
        res.extend(subglist) 
        return res

def same_type(f):
    def decorated(*args):
        type_in = type(args[0])
        for obj in args:
            if type(obj) != type_in:
                print("Обнаружены различные типЫ!")
                return 
        return f(*args)
    return decorated

@same_type
def a_plus_b(a, b):
    return a + b

def task_generate_circel():
    pass

def main():
    #print(can_eat((2,1),(4,2)))
    #print(is_prime(13))
    #matr_cheak(5,3)
    #print(make_matrix((4,6),7))
    #enter_results(1,2,3,4,5,6,7,8)
    #task_5()
    #print(recursive_digit_sum(123456))
    #print( merge_sort([7,5,2,3,9,8,6]))
    #print(make_linear([[1],[2,3],[4,6]]))
    #print(a_plus_b("5",6))
    di = {}
    di[0] = "frog"
    print(di)
    pass

if __name__ == "__main__":
    main()

