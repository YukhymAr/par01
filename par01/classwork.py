# ітерація - одне виконання тіло цикла
for i in range(1, 6, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)
n = int(input())
for i in range(1, n + 1):
    print(i)
n = int(input())
i = 1
while i <= n:
    print(i)
    i += 1 #інкреент збільшення на один 2. декриент - зеньшення на один

n = int(input())
suma = 0
for i in range(1, n + 1):
    suma += i
print(f'Сума = {suma}')
n = int(input())
for i in range(1, n + 1):
n=int(input())
count=0
for i in range(1, n + 1):
    if i % 2 == 0:
    count += 1
print(f"Парних чисел {count}")

while True:
    n = int(input('введіть число обо слов "0"')
    if n ==0:
         break
 print(f'введено число {n}')
for i in range(1,11):
    continue
    print(i)
digit_last = n % 10
digit_first = n % 100
if digit_last == digit_first:
print('ok')
while n > 0:
    d1g1t = n % 10
    print(d1g1t)
    n = n // 10
    n //= 10
max_digit = 0
while n > 0:
    d1g1t = n % 10
    if d1g1t > max_digit:
         max_digit = d1g1t
n = n // 10

for i in range(1, 5):
    for j in range(1, 6):
        print(i, j)

width = 6
height = 4
for row in range(height):
#   for col in range(width):
#       print('*', end='')