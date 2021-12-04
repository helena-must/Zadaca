mikrovalna = 1.3
vrijeme = 2 * 30
cijena = 0.46

potrosnja = mikrovalna * vrijeme
mj_cijena = potrosnja * cijena
print("Mjesecna cijena je {} kuna.".format(mj_cijena))
print("Mjesecna potrosnja je {} kW.".format(potrosnja))

import math
a = 3
sq_root = math.pow(3, 0.5)
Va = a*sq_root / 2
povrsina = (a*Va) / 2
opseg = a + a + a
print("Povrsina trokuta je {}.".format(povrsina))
print("Opseg trokuta je {}.".format(opseg))