from person import Person

pe1=Person("Teppo","Testi","Alku")

print(pe1.getFname())
pe1.setFname("Jussi")
print(pe1.getFname())

pe1.__fname="Antti"
print(pe1.getFname())

print(pe1.getPublicName())
pe1.publicName="Loppu"
print(pe1.getPublicName())
print(pe1.publicName)