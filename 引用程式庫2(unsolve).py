#problem unsolve
#import math (下面要改math.pi)
r = input('請輸入半徑 ')
area = 0
def cirArea():    
    global area
    global r
    area = 3.14 * r * r#(=r**2)
    return area
print('圓面積= %.2f' %area)#取道小數點後兩位
    