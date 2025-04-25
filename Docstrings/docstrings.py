class dog():
  def __init__(self, name,breed):  

    """This is a method that initializes the dog object with a name and breed."""
    self.name=name
    self.breed= breed
    """Thsii is the name and breed of the dog"""
dog= dog('silky', 'gali ki nasal')
print(dog.name)
print(dog.breed)

print(help(dog))