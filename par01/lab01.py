#A

a = int(input())
if a % 2 == 0:
    print("Парне")
else:
    print("Непарне")

#B

vik = int(input("Вік: "))

if vik > 18 :
    print("Ви повнолітні")
else:
    print("Ви не повнолітні")
#C

rad = int(input("Введіть радіус: "))
light = 2 * rad * 3.14
area = 3.14 * (rad ** 2)

print(light)
print(area)

#D

a = int(input())
b = int(input())

if a > b :
    print(a)
else:
    print(b)

#2
x = int(input())
y = int(input())

if (x > 0 and y > 0 ):
    print("1")
elif (x < 0 and y > 0 ):
    print("2")
elif (x < 0 and y < 0):
    print("3")
elif (x > 0 and y < 0):
    print("4")

#3
age = int(input("Введіть вік: "))
if age % 10 == 1 and age % 100 != 11:
    print("рік")
elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
    print("роки")
else:
    print("років")

#4

N = int(input())
k = 10
p1 = 17
p2 = 120

fl = N // k
rs = N % k

opt1 = fl * p2 + rs * p1

print(min(opt1))