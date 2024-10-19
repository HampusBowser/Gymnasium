
# Dictionary över platserna i flygplanet
seats = {
  "A1": "",
  "A2": "",
  "A3": "",
  "A4": "",
  "B1": "",
  "B2": "",
  "B3": "",
  "B4": "",
  "C1": "",
  "C2": "",
  "C3": "",
  "C4": "",
  "D1": "",
  "D2": "",
  "D3": "",
  "D4": "",
  "E1": "",
  "E2": "",
  "E3": "",
  "E4": ""
}

# Printar ut en meny och tar in en inmatning från användaren.
def menu():
    choice = int(input("""Varsågod välj:
    1. Skriv ut flygplanets platser
    2. Boka plats
    3. Söka efter plats
    4. Söka efter namn
    5. Avsluta
    skriv siffra här: """))
    return choice

# Skriver ut alla platser och passagerare i flygplanet.
def printPassengers():
    for seat in seats:
        print("Seat: "+seat+" passenger: "+seats.get(seat))

# Kollar upp om angivet säte är tillgängligt och om det är fallet så bokas sätet. Undantaget är vid nödutgångssätena där en ytterligare check görs för åldern.
def chooseSeat():
    name = input("Skriv in efternamn: ")
    chosenSeat = input("Var vill du sitta? ")
    passenger = seats.get(chosenSeat)
    if passenger == "":
        if chosenSeat == "C1" or chosenSeat == "C2" or chosenSeat == "C3" or chosenSeat == "C4":
            question = input("Är du 16 år eller över? [Y/N]: ")
            if question == "N":
                print("Sätet tillåter endast 16+")
                return
        seats.update({chosenSeat:name})
    else:
        print("Säte upptaget")

# Kollar om angivna sätet är upptaget eller inte och meddelar användaren.
def searchSeat(seat):
    passenger = seats.get(seat)
    if passenger == "":
        print("Platsen är tom")
    else:
        print("Platsen är inte tom")  

# Går igenom alla platser och meddelar ifall den angivna passageraren är på planet.
def searchPassenger(passenger):
    for seat in seats:
        if seats.get(seat) == passenger:
            print("Personen du sökte efter sitter på plats: " + seat)
            return
    print("Personen du sökte efter har ingen plats.")


# Huvudloopen för programmet körs till användaren väljer att avsluta. Här kallas alla funktioner.
quit = False
while not quit:
    choice = menu()
    if choice == 1:
        printPassengers()
    elif choice == 2:
        chooseSeat()
    elif choice == 3:
        searchSeat(input("Säte att söka efter: "))
    elif choice == 4:
        searchPassenger(input("Skriv in person du söker efter: "))
    elif choice == 5:
        quit = True
    else:
        menu()
print("Program avslutat!")