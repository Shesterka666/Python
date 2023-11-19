def solve():
    n = int(input())
    l = ['а','б','в']
    #li = set("абв")
    #S = 'абв'
    for _ in range(n):
        s = input()
        if not s[0].lower() in l:
            print("NO")
            return
    print("YES")

def solve2():
    n = int(input())
    for _ in range(n):
        s = input()
        if "##" == s[:2]:
            s = s[2:]
            print(s)
            continue
        if "@@@" == s[-3:]:
            continue
        print(s)

def solve3():
    s = input()
    print(*set(s), sep='')
    print("".join(set(s)))

def solve4():
    n = 3
    d= dict()
    d = {}
    for _ in range(n):
        s = input()
        for word in s.split():
            if word in d:
                d[word] += 1
                continue
            d[word] = 1
    for el in d:
        print(el, d[el])

if __name__ == "__main__":
    #solve()
    a = [i**2 for i in range(1,6)]
    print(a)
    a = (i**2 for i in range(1,6))
    print(next(a))