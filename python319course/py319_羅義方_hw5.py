class Student:
    def __init__(self,name,gender):
        self.name= name
        self.gender= gender
        self.score= []
    def avg(self):
        return sum(self.score)/len(self.score)
    def add(self,score):
        self.score.append(score)
    def fcount(self):
        i = 0
        j = 0
        while i < len(self.score):
            if self.score[i]<60:
                j = j+1
            i = i+1
        return j
    def __str__(self):
        return f"Name:{self.name} Avg:{self.avg()} 不及格:{self.fcount()}"
    @classmethod
    def top(cls, *students):
        tops=[]
        name=[]
        i = 0
        while i < len(students):
            tops=tops+[students[i].avg()]
            name=name+[students[i].name]
            i+=1
        ts=0
        ind=0
        for j in range(0,len(students)-1):
            if students[j].avg()>ts:
                ts=students[j].avg()
                ind=j
        print("最高分的同學是:",name[ind],"平均:",tops[ind])
s1 = Student("Tom","M")
s2 = Student("Jane","F")
s3 = Student("John","M")
s4 = Student("Ann","F")
s5 = Student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

tops = Student.top(s1,s2,s3,s4,s5)
