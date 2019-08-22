print('乘法表')
num = input('請輸入一個自然數')
while not num.isdigit():
    print('請輸入一個\'自然數\'' , end = ' ')
    num = input()
mode = input('press 1 for, press 2 while ')
while mode != '1' and mode!= '2':    
    print('press 1 for, press 2 while' , end = ' ')
    mode = input()
else:    
    i = 1
    j = 1
    num = int(num)
    if mode == '1': 
        for i in range(1,num + 1):
            for j in range(1,num + 1):
                print('%d * %d = %d' %(i,j,i*j))
                j += 1
            i += 1
    elif mode == '2':
        while i <= num:
            while j <= num:
                print('%d * %d = %d' %(i,j,i*j))
                j += 1
            j = 1
            i += 1