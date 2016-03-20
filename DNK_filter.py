spremenljivka = open ("DNK.txt").read()

print "Dolzina DNK vijacnice:" + str(len(spremenljivka))

print "Barva las crna:", spremenljivka.find("CCAGCAATCGC")
print "Barva las rjava:", spremenljivka.find("GCCAGTGCCG")
print "Barva las korencek:", spremenljivka.find("TTAGCTATCGC")

print "Kvadratna oblika obraza:", spremenljivka.find("GCCACGG")
print "Okrogla oblika obraza:", spremenljivka.find("ACCACAA")
print "Ovalna oblika obraza:", spremenljivka.find("AGGCCTCA")

print "Modra barva oci:", spremenljivka.find("TTGTGGTGGC")
print "Zelena barva oci:", spremenljivka.find("GGGAGGTGGC")
print "Rjava barva oci:", spremenljivka.find("AAGTAGTGAC")

print "Moski spol:", spremenljivka.find("TGCAGGAACTTC")
print "Zenski spol:", spremenljivka.find("TGAAGGACCTTC")

print "Belec:", spremenljivka.find("AAAACCTCA")
print "Crnec:", spremenljivka.find("CGACTACAG")
print "Azijec:", spremenljivka.find("CGCGGGCCG")


