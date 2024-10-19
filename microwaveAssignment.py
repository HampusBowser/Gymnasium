# Räknar ut energi med hjälp av angiven tid och watt.
def energyConsumption(time, watt):
    energy = time*60*watt
    return energy

# Räknar ut kostnaden med hjälp av angiven energi och elpris.
def cost(energy):
   return energy/kWhToJoule*electricityPrice

# Elpriset i öre.
electricityPrice = 189

# Variabel som används i "cost" funktionen.
kWhToJoule = 3600000

# Variabler för hur personerna använder mikrovågsugnen (min, watt)
emilEnergy = energyConsumption(2.5, 800)
andreasEnergy = energyConsumption(3.5, 800)
mikaelEnergy = energyConsumption(0.5, 600)
kennethEnergy = energyConsumption(0.5, 600)

# Hur mycket energianvändandet av mikrovågsugnen kostade i öre.
emilPrice = cost(emilEnergy) 
andreasPrice = cost(andreasEnergy)
mikaelPrice = cost(mikaelEnergy)
kennethPrice = cost(kennethEnergy)

# Variabel med namnet för varje persons maträtt.
emilFood = "röd pölse"
andreasFood = "köttbullar med mos"
mikaelFood = "restaurangmat1"
kennethFood = "restaurangmat2"

# Printar allt.
print("Emil mat: " + emilFood + " Energi: " + str(emilEnergy) + "J  Kostnad: " + str(emilPrice) + " öre")
print("Andreas mat: " + andreasFood + " Energi: " + str(andreasEnergy) + "J  Kostnad: " + str(andreasPrice) + " öre")
print("Mikael mat: " + mikaelFood + " Energi: " + str(mikaelEnergy) + "J  Kostnad: " + str(mikaelPrice) + " öre")
print("Kenneth mat: " + kennethFood + " Energi: " + str(kennethEnergy) + "J  Kostnad: " + str(kennethPrice) + " öre")
