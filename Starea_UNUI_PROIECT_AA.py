from enum import Enum
class Stare (Enum):
    NOU = 'nou'
    LUCRU = 'lucru'
    GATA = 'gata'
s = Stare('nou')
print (s.name)
print (s.value)
print (s == Stare.GATA)