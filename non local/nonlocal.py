def count():
    text =("This is an example of nonlocal variable it can be accesees inside of a function ,While the local can not!")
      
    def basil_is_noob():
        nonlocal text
        print(text)
    basil_is_noob()

count()