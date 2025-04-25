try:
    result=1 / 0
except ZeroDivisionError as e:  
    print("Error: Division by zero is not allowed.")
finally:
    result = 1
print(result)    




#raise
try:
    raise Exception("An error stating ...bla bla bla")
except Exception as error:
    print(error)