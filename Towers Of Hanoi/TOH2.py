from dataclasses import dataclass
from collections import deque


deques = []
n = 4
posts = {"1":None, "2": None, "3": None}

small_deque = deque(range(1,3))

deques.append(small_deque)
for x in range(2,n+1):
    deques.append(deque(range(3)))
    
def little_move(discs):
    pass
    
    
    
print(deques[2][0])
deques[2].rotate(-1)
print(deques[2][0])
deques[2].rotate(-1)
print(deques[2][0])
deques[2].rotate(-1)
print(deques[2][0])
deques[2].rotate(-1)
print(deques[2][0])
deques[2].rotate(-1)
print(deques[2][0])
print(len(deques))