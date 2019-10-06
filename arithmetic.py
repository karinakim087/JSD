def sum(a, b):
    q=[]
    z=len(a)
    x=len(b)
    if z > x:
            b = [0] * (z - x) + b
            for i in range(0,z).__reversed__():
                if a[i]+b[i]>=10:
                    q.append(a[i]+b[i]-10)
                    b[i-1]=b[i-1]+1
                else:
                    q.append(a[i] + b[i])
            q.reverse()
            print('Сумма чисел равна', q)
    elif z<x:
            a = [0] * (z - x) + a
            for i in range(0, x).__reversed__():
                if a[i] + b[i] >= 10:
                    q.append(a[i] + b[i] - 10)
                    a[i - 1] = a[i - 1] + 1
                else:
                    q.append(a[i] + b[i])
            q.reverse()
            print('Сумма чисел равна', q)
    else:
            for i in range(0, x).__reversed__():
                if a[i] + b[i] >= 10:
                    q.append(a[i] + b[i] - 10)
                    a[i - 1] = a[i - 1] + 1
                else:
                    q.append(a[i] + b[i])
            q.reverse()
            print('Сумма чисел равна', q)
def dif(a,b):
    w = []
    z = len(a)
    x = len(b)
    if z > x:
            b = [0] * (z - x) + b
            for i in range(0,z).__reversed__():
                if a[i] - b[i] < 0:
                    w.append(a[i] - b[i] + 10)
                    b[i - 1] = b[i - 1] - 1
                else:
                    w.append(a[i] - b[i])
            w.reverse()
            print('Разность чисел равна', w)
    elif z<x:
        a = [0] * (z - x) + a
        for i in range(0, x).__reversed__():
            if b[i] - a[i] < 0:
                w.append(b[i] - a[i] + 10)
                a[i-1] = a[i-1]-1
            else:
                w.append(a[i] - b[i])
        w.reverse()
        print('Разность чисел равна', w)
    else:
        l=0
        while True:
            if a[l]>b[l]:
                for i in range(0,z).__reversed__():
                    if a[i] - b[i] < 0:
                        w.append(a[i] - b[i] + 10)
                        b[i - 1] = b[i - 1] - 1
                    else:
                        w.append(a[i] - b[i])
            w.reverse()
            print('Разность чисел равна', w)
            break
        else:
            if b[i] - a[i] < 0:
                w.append(b[i] - a[i] + 10)
                a[i - 1] = a[i - 1] - 1
            else:
                w.append(a[i] - b[i])
            w.reverse()
            print('Разность чисел равна', w)