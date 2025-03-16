class Person:#默认继承object
    def __init__(self,name,age):
        self.name=name
        self.__age=age   #年龄不能在类的外部使用（private），只能通过类内函数调用
    def show(self):
        print(self.name,end='\t')
class Student(Person):
    def __init__(self,name,age,stu_num):
        super().__init__(name,age)
        self.stu_num=stu_num
    def show(self):
        super().show()    #方法重写
        print(self.stu_num)
stu1=Student('ll',20,1001)
stu1.show()
#print(dir(stu1))        #查看指定对象所有属性
#类外访问private
#print(stu1._Student__age)