class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return True if self.age> other.age else False



silky=('silky',3)
oreo=('oreo',4)

print(silky<oreo)
print(oreo<silky)