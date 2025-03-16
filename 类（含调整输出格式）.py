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


p1 = People('Jack', 'Shanghai')
p2 = People('Peter', 'New York')
p3 = People('Lucy', 'London')
p4 = People('Ann', 'Tokyo')
persons = [p1, p2, p3, p4]
print('Original:', persons)
persons.sort()
print('Sorted:', persons)




