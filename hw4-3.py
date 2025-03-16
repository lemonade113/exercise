class Mylist(list):
    def product(self):
        k = 1
        for i in self:
            k = k*i
        return k


