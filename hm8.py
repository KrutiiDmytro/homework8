# Задание 1
# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
lst = [0] * 50
lst[0] = lst[-1] = 1
print(lst)
# Задание 2
# Сформировать возрастающий список из чётных чисел (количество элементов 45)
sps = list(range(0, 45, 2, ))
print(sps)


# Задание 3
# Пользователь вводит число. Определить, содержит ли список данное число x.
# Вивести информационное сообщение содержит или не содержит
def isin(sps1, n):
    return n in sps1


print(isin([1, 2, 3, 4, 5], 5, ))

# Задани 4
# Найдите сумму и произведение элементов списка. Результаты вывести на экран

# Задание 5
# Найти наибольший элемент списка и вывести его на экран
print(max(filter(lambda x: x & 1 == 0, [1, 2, 3, 8, 4, 5, 6, 7, ])))

# Задание 6
# Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение
lst = [1, 2, 3, 4, 5, 5, 6, 6, 7, ]
print(*filter(lambda x: lst.count(x) > 1, lst))

# Задание 7
# Поменять местами самый большой и самый маленький элементы списка;
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)

# Задание 8
# Дан произвольный список. Представьте его в обратном порядке
lst = [100, 200, 300, 400, 500]
lst2 = lst[::-1]
print(lst2)
