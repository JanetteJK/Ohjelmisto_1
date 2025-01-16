import math
luoti = input("luodit")
luoti = float(luoti)
naula = input("naulat")
naula = float(naula)
leiviska = input("leiviskät")
leiviska = float(leiviska)
LUODIT_GR = 13.3
NAULAT_GR = 32*LUODIT_GR
LEIVISKAT_GR = 20*NAULAT_GR


massa_gr = LEIVISKAT_GR*leiviska + LUODIT_GR*luoti+ NAULAT_GR*naula
kilogramma = int (massa_gr/1000)
grammat = int (massa_gr%1000)

print (f"massa nykyään {kilogramma} kg {grammat} grammaa")




