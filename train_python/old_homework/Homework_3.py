#code
#import numpy as np
import os
def task_1():
    num = int(input())
    summy = 0
    while num % 10 != 0 or num > 9:
        summy += num % 10
        num = num // 10
    print(summy)

def task_2():
    stringy = input()
    mini = stringy[0]
    for i in range(len(stringy)):
        if stringy[i] > mini:
            mini = stringy[i]
    print(mini)

def task_3():
    stringy = input()
    mini = ""
    for i in range(len(stringy)):
        if int(stringy[i]) % 2 !=0:
            mini += stringy[i]
    print(mini)

def task_4():
    step = num = 500
    counter_for_win = 0
    print(num)
    while(text := input()) != "угадал":
        if counter_for_win == 10:
            print("Ти проиграл. эххх")
            return
        step =round(step/2)
        match text:
            case "меньше":
                 num -= step
                 counter_for_win += 1
            case "больше":
                 num += step
                 counter_for_win += 1
        if num > 1000:
            num = 1000
        if num < 0:
            num = 1
        print(num)
        
def task_6():
    stroka_1 = input()
    stroka_2 = input()
    stroka_3 = input()
    zaika = "зайка"
    glist = []
    if zaika in stroka_1:
        glist.append(stroka_1)
    if zaika in stroka_2:
        glist.append(stroka_2)
    if zaika in stroka_3:
        glist.append(stroka_3)
    buufer = min(glist)
    print(buufer, len(buufer))
    #print(value:= min(filter(lambda x: zaika in x, (stroka_1,stroka_2,stroka_3))), len(value))

def task_resheto(glist: list) -> list:
    nw = []
    for i in range(len(glist)):
        for j in range(2, int(glist[i])):
            if glist[i] % j == 0:
               break
        else: nw.append(glist[i])
            #else: nw.remove(glist[i])
    return nw
    
def task_7():
    n = int(input())
    glist = []
    for i in range(n):
        glist.append(int(input()))
    nw = task_resheto(glist) 
    print(nw)

def task_8():
    n = int(input())
    m = int(input())
    massy = []
    for i in range(n):
        ma= []
        for j in range(m):
                ma.append(j * n + 1 + i)
        massy.append(ma)
    
    for row in massy:
        print(*row)

    #for i in range(n):  
       # for j in range(m):  
          #  print(massy[i][j], end = " ")  
       # print() 

def task_9():
    n = int(input())
    glist = []
    for i in range(3):
        s = input().lower().replace(" ","")
        if s == s[::-1]:
            glist.append(s)
    print(len(glist))

def task_10():
    n = int(input())
    a = [[min(i + 1, n - i, j + 1, n - j) for j in range(n)] for i in range(n)]
    for row in a:
        print(*row)

def help(chislo):
    buufer = int(chislo)
    return buufer > 0

def task_5():#будут только целые - точку в регулярку и хвостатую туда же
    reg = ":;,./?!=-+-"#ето так .. текст почистить
    try:
        with open("python.txt") as feale:
            text = feale.read()
    except: return
    for charochka in reg:
        text.replace(charochka, "")
    chisla = text.split()
    summy = sum(map(int,chisla))
    sred = summy/len(chisla)
    print("Количество всех чисел:",len(chisla))
    #print("Количество всех + чисел:",len(list(filter(help,chisla))))
    print("Количество всех + чисел:",len(list(filter(lambda x: int(x) > 0,chisla))))
    print("Минимальное число:",min(map(int,chisla)))
    print("Максимальное число:", max(map(int,chisla)))
    print("Сумма всех чисел:",summy)
    print("Среднее арифметическое:",round(sred,2))

def disk_x(b: float, d: float, a:float, plus:bool) -> float:
    if d == 0.0:
        return -1*(b/(2*a))
    elif plus:
        return (-1*b + d**(1/2))/(2*a)
    else:
        return (-1*b - d**(1/2))/(2*a)

def task_11():
    a = float(input())
    b = float(input())
    c = float(input())
    solution = list()
    d = b*b-4*a*c
    #print("a",a,"d",d)
    if a == 0.0 and b==0.0 and c ==0.0:
        print("Infinite solutions")
        return
    elif d == 0.0:
        x = -1*(b/(2*a))
        solution.append(disk_x(b,d,a,True))
        print(format(solution[0],".2f"))
        return
    elif d > 0.0:
        solution.append(disk_x(b,d,a,True))
        solution.append(disk_x(b,d,a,False))
    else:
        print("No solution")
        return
    solution.sort()
    print(round(solution[0],2),round(solution[1],2))

def task_12():
    #s = '᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!'
    #res = ''.join(chr(ord(i) & 255) for i in s))
    #print(res)
    path = input("Введите путь к файлу: ")
    if not os.path.exists(path):
         print("Фигня, нет файла!")
    else:
        with open("python2.txt","r",encoding="utf8") as feale:
            text = feale.read()
        res = ''.join(map(lambda i: chr(ord(i)%128), text))
        print(res)
       
def main ():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()
    task_11()
    task_12()

if __name__ == "__main__":
    main()
