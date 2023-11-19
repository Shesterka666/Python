def print_ne(s):
    return print(s + " - это не число")

def task_1(string):
    return print(string[::-1])

def proverka_na_chislo(x):
    try:
        return int(x)
    except:
        return print_ne(x)

def task_help(x, y):
    if type(proverka_na_chislo(x)) != int:
        return
    if type(proverka_na_chislo(y)) != int:
        return
    return print(y + " " + x)

def task_2(string):      
     return task_help(string.split(" ")[0], string.split(" ")[1])

def task_2_1():
    s = input()
    ind = s.find(' ')
    print(s[:ind + 1], s[:ind])

def task_3_1(n):
    nn = proverka_na_chislo(n)
    for _ in range(nn):
        list = ["*" for x in range(nn)]
        print(*list)

def task_3(n):
    nn = proverka_na_chislo(n)
    if type(proverka_na_chislo(n)) != int:
        return
    else:
        for i in range(nn):
            for j in range(nn):
                print("*", end="\t")
            print()

def task_4(x):
    try:
        if int(x) <= 999 or int(x) >= 10000:
            return print("Вы ввели не четрзнач")
        else: 
            return(print(x[1] + x[0] + x[3] + x[2]))
    except:
        print("Вы ввели не число :(")
def task_5():
    #x = int(input())
    #y = int(input())
    x = "405"
    y = "839"
    summy = 0
    a = (int(x[0]) + int(y[0]))%10
    b = (int(x[1]) + int(y[1]))%10
    c = (int(x[2]) + int(y[2]))%10
    print(f"{a}{b}{c}")

def task_5_1():
    a = int(input())
    b = int(input())
    edn = (a + b) % 10
    a //= 10
    b = b // 10
    dec = (a + b) % 10
    a //= 10
    b = b // 10
    sot = (a + b) % 10
    print (sot, dec, edn, sep="")

def task_6(red: int, green: int , blue: int):
    task = red + blue + 1
    return print(task)

def task_7(A: int, B: int, C: int):
    task = abs(B - A)/C
    return print(task)

def main():
    task_1(input())
    task_2(input())
    task_3(input())
    task_3_1(input())
    task_4(input())
    task_5()
    task_6(int(input()),int(input()),int(input()))
    task_7(int(input()),int(input()),int(input()))

if __name__ == "__main__":
    main()