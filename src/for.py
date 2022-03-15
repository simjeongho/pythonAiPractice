
num = int(input("Multiplication table of : "))
for i in range(1,10): print(num, 'x', i, '=', num * i) # for 문 for ~ in~ range

#이중 포문
for i in range(2,10):
    for j in range(1,10):
        print("%2d x %2d = %5d" %(i,j,i*j) )
    print("-----------------")