x = "awesome" # This x is global

def myfunc():
  x = "fantastic" #However, that x is local
  print("Python is " + x)

myfunc() # outputs Python is fantastic

print("Python is " + x) # outputs Python is awesome