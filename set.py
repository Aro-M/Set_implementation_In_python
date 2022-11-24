import  random
class Set:
    def __init__(self,value= []):
        self.data = []
        self.concat(value)

    def intersect(self,other):
        res = []
        for x  in self.data:
            if  x in other:
                res.append(x)
        return  Set(res)

    def union(self,other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self,value):
        for x in value:
            if  not x in self.data:
                self.data.append(x)

    def difference(self,other):
        res = []
        for  i in self.data:
            if not i  in other.data:
                res.append(i)
        return  res

    def  issubset(self,other):
        count = 0
        for  i in self.data:
            if  i in other.data:
                count += 1
                if  len(self.data) == count:
                    return True
            else:
                return False

    def remove(self,value):
        for i in self.data:
            if  i  == value:
                self.data.remove(i)
        return self.data

    def  pop(self):
        self.data.pop(random.randrange(len(self.data)))

    def __copy__(self,other):
        self.data = other.data.copy()
        return  self

    def  clear(self):
        del self.data[0:len(self.data)]
        return self

    def __len__(self):
        return  len(self.data)

    def  __getitem__(self, item):
        return  self.data[item]

    def  __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def  __repr__(self):
        return '<Set:' + repr(self.data) + ">"

# users1 = Set(['Bob', 'Emily', 'Howard', 'Peeper'])
# users2 = Set(['Jerry', 'Howard', 'Carol'])
# users3 = Set(['Emily', 'Carol'])
# print(users1 & users2)
# print(users1 | users2)
# print(users1 | users2 & users3)
# print((users1 | users2) & users3)
# print(users1.data)
# print(users1.__repr__())
# print(users1.remove("Bob"))
# users1.pop()
# print(users1)
# print(users1.clear())
# print(users1[1])
# print(users1.__copy__(users2))
# print(users1)
# print(len(users1))
# print(users1.issubset(users2))
# print(users1.difference(users2))
# print(users1.union(users2))