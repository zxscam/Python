"""
Задание 9.
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
k = 0
for z in range(int(input())):
    if int(input()) == 0:
        k+=1
print(k)