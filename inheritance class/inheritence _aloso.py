class walking:
    def meso_is_watching(self):
        print("Meso is watching")


class meso():
    def meso_is_betch(self, name, age):
        self.name = name
        self.age = age
        print(f'{self.name} is the biggest betch and he is {self.age} years old')
print(meso.meso_is_betch)

meso_instance = meso()

meso_instance.meso_is_betch('messam', 2)

walking_instance = walking()
walking_instance.meso_is_watching()