for i in range(1, 21):
    print(i)
print("work 2 ")
sum = 0
for i in range(1, 1000000):
    sum += i
print(sum)
for i in range(1, 20 , 2):
    print(i)

lifang = [var ** 3 for var in range(1, 10)]
print(lifang)



zimu = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # 浅层拷贝
# tmp = zimu[-3:]
# print(tmp)

zimus = zimu
print(zimus)
print(zimu)
zimus[0] = 'HHHH'
print(zimus)
print(zimu)