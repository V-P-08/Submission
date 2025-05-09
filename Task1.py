try :
    List1 = {'Alice':89,'Sarah':78,'Liam':95,'Badger':87,'Kyle':77,'Marco':99,'Katie':99}
    name = input("Enter student's name: ")
    print(List1[name])
except :
    KeyError
    print("Student not found")
