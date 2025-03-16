class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def __str__(self):
        return '({0},{1})'.format(self.name, self.city)
    def moveto(self, newcity):
        self.city = newcity
    def __lt__(self, other):
        return self.city < other.city
    __repr__ = __str__


class Teacher(People):
    def __init__(self, name, city, school):
        super().__init__(name, city)
        self.school = school
    def newschool(self, newschool):
        self.school = newschool
    def __lt__(self, other):
        return self.school < other.school
    def __repr__(self):
        return '(%s,%s)'%(self.name, self.school)


p1 = Teacher('Jack', 'Shanghai', '上大')
p2 = Teacher('Peter', 'New York', '纽大',)
p3 = Teacher('Lucy', 'London', '伦大')
p4 = Teacher('Ann', 'Tokyo', '东大')
teachers = [p1, p2, p3, p4]
print('Original:', teachers)
teachers.sort()
print('Sorted:', teachers)
