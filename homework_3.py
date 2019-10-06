#Задача 1
#Удалить из списка все повторяющиеся значения, оставив их первые вхождения, т.е. в
#списке должны остаться только различные элементы. Не использовать
#дополнительные структуры, такие как dict или set.
#Пример. Список [2, 'cat', 7, 2, 9, 'cat', 7, 42] после удаления повторяющихся элементов
#будет таким [2, 'cat', 7, 9, 42].
def DeleteDuplicates(a):
    for i in a:
        if a.count(i)>1:
            a.reverse()
            del a[a.index(i)]
            a.reverse()
    print(a)
DeleteDuplicates([2,'cat',7, 2, 9, 'cat', 7, 42])
#Задача 2
#Для арифметических операций с большими числами, которые не могут быть
#редставлены в памяти компьютера, используется следующий прием. Каждая цифра
#аких чисел записывается в отдельный элемент списка, и необходимые операции
#проводятся с элементами списка цифр. Написать функцию, принимающую на вход два
#списка цифр:
#1 Выполняющую сложение двух чисел, состоящих из одинакового количества
#наков.
# Выполняющую вычитание двух чисел, состоящих из одинакового количества
#знаков.
#3 Выполняющую сложение двух чисел, состоящих из произвольного количества
#знаков.
#4 Выполняющую вычитание двух чисел, состоящих из произвольного количества
#знаков.
#Пример. Числа 8953 и 2721 можно представить как списки [8, 9, 5, 3] и [2, 7, 2, 1], в результате
#сложения получим [1, 1, 6, 7, 4]. Алгоритм сложения/вычитания такой же, как
#сложение/вычитание столбиком на листочке.
#Комментарий. Пункты 1 и 2 являются частным случаем пунктов 3 и 4, поэтому у кого получится
#сразу сделать 3 и 4, можно не делать 1 и 2
import arithmetic
def answer(a,b):
    print(arithmetic.sum(a,b),
          arithmetic.dif(a,b))
answer([6,7,8],[1,2,3])