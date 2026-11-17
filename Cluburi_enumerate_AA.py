from enum import Enum 
class Club (Enum):
    ROBOTICA =1
    ARTA=2
    SPORT =3
cod:Club = Club(int(input('cod= ')))
print (cod.name)
print (cod==Club.ROBOTICA)