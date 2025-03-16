class Student:
    #类属性
    stu_num=3456
    stu_sex='女'
    #初始化
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "我的名字是{0}，今年{1}岁了".format(self.name,self.age)
    #实例方法
    def grades(self):
        print(self.name,'whatever')
    @staticmethod
    def static_():
        print('static')
    @classmethod
    def class_(cls):
        print('class')

stu1=Student('zhangan',20)
stu2=Student(20,78)
'''
#不同的访问方法
stu1.grades()
Student.grades(stu1)

#动态绑定属性
stu1.sex='女'
print(stu1.name,stu1.age,stu1.sex)
#动态绑定方法
def show():
    print('动态绑定')
stu1.show=show
stu1.show()

print(stu1.name,stu1.age)

print(Student.stu_sex)
print(stu1.stu_sex)

#静态方法和类方法的访问
Student.class_()
Student.static_()
'''
print(stu1)