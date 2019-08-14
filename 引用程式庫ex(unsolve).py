import random
right = ['well done','great','good','bravo','fabulous']
print(random.choice(right))

print(random.randint(1,50)) #include 1 and 10

print(random.randrange(100))#from 0~'99'

random.shuffle(right)
print(right)

#"to be solved~"
# random.seed(5)
# i = 0
# for i in range(6)
#     print(random.randrange(10))
