num=int(input('Enter the number: '))
for i in range(num-1,-1,-1):
    for j in range(i+1):
        print('*', end=' ')
    print()
