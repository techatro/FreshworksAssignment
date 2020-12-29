from crud import CRUD

#print(crud.create('age','20'))

x = CRUD()

print(x.read())

print(x.create("college","Mahendra College of Engineering"))

print(x.read())

print(x.update("college","Mahendra Engineering College"))

print(x.delete("college"))
