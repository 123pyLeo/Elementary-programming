class Student:
    count = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

student1 = Student('LinTao', 100)
student2 = Student('LiuTong', 59)
student3 = Student('XiuCai', 0)

student1.print_score()
student2.print_score()
student3.print_score()

print("总共实例化了 %d 个学生" % Student.count)