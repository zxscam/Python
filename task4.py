<<<<<<< HEAD
def count(n):
    i = 0
    while i < n + 1:
        print(i)
        i += 1
count(10)
=======
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
"""
def power(a, n):
    if n == 0:
        return 1
    else:
        return a*power(a, n - 1)

print(power(float(input()), int(input())))
>>>>>>> def
