import numpy as np
import pandas  as pa
import math
import re
from typing import Union, Tuple

def task_1(s):
    lst = s.split()
    pr = math.prod(map(int, lst))
    count = len(lst)
    return pr**(1/count)

def task_2():
    Doki = list(map(float,input().split()))#вводим сначала x потом y
    Poli = list(map(float,input().split()))#вводим ро потом фи. Считаем что фи всегда второй
    #переводим всьо в доку, а то в полярной там ойеойоеой
    new_x = math.cos(Poli[1])*Poli[0]
    new_y = math.sin(Poli[1])*Poli[0]
    tas = ((new_x - Doki[0])**2 - (new_y - Doki[1])**2)**0.5
    print(tas)

def multiplication_matrix(n:int):
    return  [[i*j for j in range(1,n+1)] for i in range(1,n+1)]

def stairs_matrix(n:int):
    a = [[abs(i-j) for j in range(n)] for i in range(n)]
    for i in range(n):  
        for j in range(n):  
            print(a[i][j], end = " ")  
        print() 

def length_stats(text: str) ->Tuple[pa.Series,pa.Series]:
    data = sorted(filter(lambda x: x, re.split(r"\s+", re.sub(r"[^а-яa-z]", " ", str.lower(text)))))
    data = set(data)  
    data = list(data)
    res = np.array_split(data,2)   
    return (pa.Series(data=list(map(len, res[0])), index=res[0], dtype=np.int64),pa.Series(data=list(map(len, res[1])), index=res[1], dtype=np.int64))

def cheque(price_list, **kwarg):
    dic = {"price":price_list, "number": kwarg}
    #print(price_list)
    #print(kwarg)
    #print(type(kwarg))
    price = pa.DataFrame(dic)
    price["cost"] = price["number"]*price["price"]
    price = price.reset_index().rename(columns={'index':'product'})
    price = price.dropna()
    return price

def task_3():#нужна трассировка
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pa.Series(prices, products)
    #print(price_list)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    
    print(result)

def best(journal):#сделал плоха :( зависимость от столбцов если добавят что-то или уберут == капут
    return journal[(journal.maths >= 4) &(journal.physics >= 4)&(journal.computer_science >= 4)]

def task_4():
    columns = ['name', 'maths', 'physics', 'computer_science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer_science': [5, 2, 5, 4, 3]
    }
    journal = pa.DataFrame(data, columns=columns)
    filtered = best(journal)
    #filtered =journal[(journal.maths >= 4) &(journal.physics >= 4)&(journal.computer_science >= 4)]
    print(journal)
    print(filtered)

def update(df):
    df['Total'] = df.mean(numeric_only=True,axis=1)
    return df

def task_5():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pa.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered) 

def main():
    #print(task_1(input()))
    #task_2()
    #print(stairs_matrix(5))
    #odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    #print(odd)
    #print(even)
    #task_3()
    #task_4()
    #task_5()
    #ласт доеделать
    
    pass
    
if __name__ == "__main__":
    main()