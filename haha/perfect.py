
num = 0
while True:
    num += 1
    factors = []
    for i in range(1,num):
        if num % i == 0:
            factors.append(i)
    if sum(factors) == num:
        print(num)