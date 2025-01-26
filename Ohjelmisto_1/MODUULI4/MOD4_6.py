import random
import math
N = int(input("Montako pistettä laitetaan?\n"))
n = 0
repeat = 0

while repeat<= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2+y**2< 1:
        n = n+1
    repeat = repeat + 1
pii = 4 * n / N
print (f"Piin likiarvo on {pii}")













#x^2+y^2<1
#π≈4n/N