#Ex №1
r = str(input())
q=0
e=0
w=str.lower(r)
for i in range(len(w)):
    if w[i]=='ж' or w[i]=='ш':
        if w[i+1]=='ы':
            q+=1
    elif w[i]=='ч' or w[i]=='щ':
        if w[i+1]=="я":
                e+=1
    else:
        continue
print('Неправильное написание жи-ши',q ,'раз(-а)\nНеправильное написание ча-ща',e ,'раз(-а)')
#Ex №2
N=int(input())
a = [((-1)**(x+1))/x for x in range(1,N+1)]
b = [1/x for x in range(1,N+1)]
print('Изменив решение', N, 'раз(-a), мужчина будет на расстоянии', sum(a), 'км от дома, пройдя всего',sum(b),'км.\nОн потратит при этом', 5.5*sum(b),'ккал.' )