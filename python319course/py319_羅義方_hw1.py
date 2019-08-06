import os
math_pass = {'Tom','John','Mary','Jimmy','Sunny','Amy'}
eng_pass = {'John','Mary','Tony','Bob','Pony','Tom','Alice'}
all = math_pass.union(eng_pass)
o_math_pass = all.difference(eng_pass)
print('Q1.Ans')
print('只有數學及格的有')
print(o_math_pass)
o_eng_pass = all.difference(math_pass)
print('只有英文及格的有')
print(o_eng_pass)
allpass = eng_pass.intersection(math_pass)
print('兩科都及格的有')
print(allpass)
print('全班共有 %d 個同學' % len(all))
Tom = [80,100,90,95]
John = [100,93,75,80]
hw = {'Tom':Tom,'John':John}
avg_Tom = sum(hw['Tom'])/len(hw['Tom'])
avg_John = sum(hw['John'])/len(hw['John'])
print('Q2.Ans')
print('Tom的平均是: %d 分，而John的平均是 %d 分' %(avg_Tom,avg_John))
os.system('pause')