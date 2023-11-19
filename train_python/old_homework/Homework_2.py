def if_palydro(buufer):
    if buufer == buufer[::-1]:
        return "Палидром"
    else: return "Неа"

def task_1():
    s = input().replace(" ","").lower()
    return print(if_palydro(s))

def task_2():
    n = int(input())
    lst = []
    #i = 0
    counter_zaek = 0
    #while i < n:
       # lst[i] = input().lower()
       # if "зайка" in lst[i]:
       #     counter_zaek += 1
       # i += 1
    for i in range(n):
        lst.append(input().lower())
        if "зайка" in lst[i]:
            counter_zaek += 1
    print(counter_zaek)

def is_ok(x):
    try:
        return int(x)
    except:
        return x + " - Не число!"
 
def task_3():
    s = input()
    x = is_ok(s.split(" ")[0])
    if isinstance(x, int) != True:
        print(x)
        return
    y = is_ok(s.split(" ")[1])  
    if isinstance(y, int) != True:
        print(y)
        return
    print(x + y)
    
def task_4():#не так немного #коллизия с ключами :(
    glist = {}
    s = input()
    count = 1
    n = len(s) - 1 
    for i in range(n):
        if s[i] == s[i + 1]:
            count += 1 
            glist[s[i]] = count
        else: 
            glist[s[i]] = count
            count = 1
    print(glist)

def print_task_4(glist):
    for i, j in glist:
        print(j, i)

def task_4_fix():
    glist = []
    s = input()
    #s = '010000100001111111110111110000000000000011111111'
    count = 1
    n = len(s) 
    for i in range(n):
        if i + 1  == n or s[i] != s[i + 1]:
            glist.append((count, int(s[i])))  
            count = 1 
        else: count += 1        
    print_task_4(glist)
 
def task_5():#ханойская башня
    #s = '7 2 3 * -'
    #s = '10 15 - 7 *'
    s = input()
    glist = []# можно работать как со стэком поп и адд
    for symbol in s.split(' '):
        try:# Добавляем число если ето число
             glist.append(int(symbol))
        except:#если не число значит это знак для выполнения
            if symbol == '+':
                a = glist.pop()
                b = glist.pop()
                glist.append(b + a)
            elif symbol == '-':
                a = glist.pop()
                b = glist.pop()
                glist.append(b - a)
            elif symbol == '*':
                a = glist.pop()
                b = glist.pop()
                glist.append(b * a)       
    print(glist)

def task_5_1():#то же самое но с кейсами попробовал
    #s = '7 2 3 * -'
    #s = '10 15 - 7 *'
    s = input()
    glist = []# можно работать как со стэком поп и адд
    for symbol in s.split(" "):
        try:# Добавляем число если ето число
             glist.append(int(symbol))
        except:#если не число значит это знак для выполнения
            match symbol:
                case "+":
                    a = glist.pop()
                    b = glist.pop()
                    glist.append(b + a)
                case "-":
                    a = glist.pop()
                    b = glist.pop()
                    glist.append(b - a)
                case "*":
                    a = glist.pop()
                    b = glist.pop()
                    glist.append(b * a)   
    print(glist)

def task_6():   
    n = int(input()) 
    m = int(input())   
    manka = () #множества
    for _ in range(n):
        manka.add(input()) 
    ovksa = ()
    for _ in range(m):
        ovksa.add(input())  
    s_intersection = manka & ovksa
    if len(s_intersection) == 0:
        print("Таких нетy")
    else:
        print(len(s_intersection))

def task_8():   
    s = input()
    x = is_ok(s.split(" ")[0])
    if isinstance(x, int) != True:
        print(x)
        return
    y = is_ok(s.split(" ")[1])  
    if isinstance(y, int) != True:
        print(y)
        return
    #list = [lambda:a**2 for a in range(x, y)] не вышло :)
    list = [a**2 for a in range(x, y + 1)]
    print(list)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def task_7():   
    dict = []
    while True:
        s = input()
        if s == "":
            break
        dict.append((s.split()[0], s.split()[1]))
     
    #Сложна 1 сложность - не знал что сеты нельзя индексировать
    #Сложна 2 сложно привыкнуть к парадигме foreach на питоне
    #dict.append(("Иванов", "Петров"))    
    #dict.append(("Петров", "Яковлев")) 
    #dict.append(("Иванов", "Сергеев"))
    #dict.append(("Васильев", "Петров"))
    #dict.append(("Сергеев", "Яковлев"))
    #dict.append(("Петров", "Кириллов"))

    keys = set()
    n = len(dict)
    for i in range(n):
        s = dict[i][0] 
        keys.add(s)
        s = dict[i][1] 
        keys.add(s)
    glist = list(keys)
    glist.sort()
    buufer = []
    buufer2 = []
    n = len(glist)
    #за такое кол-во форов - убил бы сам, но как сделать проще - пока хз№
    #сложность алгоритма зашкаливает...i*(m+n*m)
    for i in range(n):# получается нашли все уникальные имена
        cur = glist[i]
        for j in range(len(dict)):#берем первое и пробуем найти первую руку
            if cur == dict[j][0]:
                buufer.append(dict[j][1])#она может быть правая проверка не нужна. так как по условию не повторяются Тимур-Лемур Лемур-Тимур
            if cur == dict[j][1]:
                buufer.append(dict[j][0])#левая ( ну условно слева или справа в введенном нами списке)
        for y in range(len(buufer)):# теперь идем искать руки найденных рук
            for g in range(len(dict)):# опять гонимся по всему списку 
                if buufer[y] == dict[g][0] and dict[g][1] != cur:#если слева нашли руку вторую и это не кур (дабы дублей не было)
                    if buufer2.__contains__(dict[g][1]) != True:#если такое имя уже есть
                        buufer2.append(dict[g][1])
                if buufer[y] == dict[g][1] and dict[g][0] != cur:# ну если нашли такую справа
                    if buufer2.__contains__(dict[g][0]) != True:# если такое есть уже 
                        buufer2.append(dict[g][0])
        buufer2.sort()#сортируем(потому как по условию надо)
        print(cur, end=": ")
        print(buufer2)# выводим красиво без фанатизма устал уже 
        buufer.clear()#чистим наши буферы наслед итерацию
        buufer2.clear()#таких будет ровно столько - сколько имен
        #но на C# яб сделал проще 
        #я бы нашел все руки 
        # И:П,С 
        # В:П 
        # С:Я,И 
        # П:Я,И,В,К
        # Я: С
        # и просто первая фамилия основная, потом руки идут знакомые
        # и дальше меняем список: И: Я,И,В,К(это П),Я,И(это С) - убираем дубли И:Я,В,К и тд
        # хотя может это и не верно - жду конфетное решение от профи питона
        
def main():
    task_1()   
    task_2()
    task_3()
    task_4_fix()
    task_5()
    #task_5_1()
    task_7()
    task_8()

if __name__ == "__main__":
    main()
