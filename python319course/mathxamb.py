import random 
import os
name= input('請輸入你的名字')
print('考生'+name+'你好')
n=1
e=0
k=0
a= random.randint(0,2)
while n < 31:
    if a == 0:
        a = random.randint(0,2)
        i = random.randint(0,1000)
        j = random.randint(0,1000)
        print('第%d題 %d * %d =' %(n,i,j))
        ans = int(input('請輸入答案'))
        if ans == i*j :
            k+=1
            print('正確')
            print('已經考驗 %d 題,正確 %d 題,錯誤 %d 題' %(n,k,e))
            n+= 1
            while k > 26:
                print('恭喜通過考驗')
                os.system('pause')
            
        else:
            print('錯誤')
            print('正確答案是 %d' %(i*j))
            e += 1
            n += 1
            if e > 3:
                print('本次考驗不及格，請等待考試人員重新設定考試')
                os.system('pause')
                os._exit()
    else:
        a = random.randint(0,2)
        i = random.randint(0,1000)
        j = random.randint(0,1000)
        print('第%d題 %d + %d =' %(n,i,j))
        ans = int(input('請輸入答案'))
        if ans == i+j :
            k +=1
            print('正確')
            print('已經考驗 %d 題,正確 %d 題,錯誤 %d 題' %(n,k,e))
            n +=1
            while k > 26:
                print('恭喜通過考驗')
                os.system('pause')
        else:
            print('錯誤')
            print('正確答案是 %d' %(i+j))
            e += 1
            print('已經考驗 %d 題,正確 %d 題,錯誤 %d 題' %(n,k,e))
            n += 1
            if e > 3:
                print('本次考驗不及格，請等待考試人員重新設定考試')
                os.system('pause')
                os._exit()