from enum import Enum 
class Culoare(Enum): 
    ROSU = 1 
    GALBEN = 2 
    VERDE = 3
cod1 = int(input('introduceti primul cod '))
cod2 = int(input('introduceti al doilea cod '))
culoare1 = Culoare(cod1)
culoare2 = Culoare(cod2)
print (culoare1.name, culoare2.name)
print (culoare1 == culoare2)