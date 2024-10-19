from tkinter import *

# Class för att hålla reda på saker rörande spelet, såsom gissningar, max gissningar och när spelet är över.
class Game:
    def __init__(self, maxGuesses):
        self.maxGuesses = maxGuesses
        self.guesses = 0

    def increaseGuesses(self):
        self.guesses += 1

    # Om man gått över tillåtna antalet gissningar eller man inte har några bokstäver
    # kvar att gissa så är spelet över och denna funktionen ger tillbaka true.
    def isGameOver(self):
        if self.maxGuesses <= self.guesses or len(charsLeftToGuess) == 0:
            return True
        else:
            return False

# Class för att skicka in värdet och göra alla linjer
class LineDraw:
    def __init__(self, x, y, x1, y1):
        self.lineDraw = canvas.create_line(x, y, x1, y1, width=3)


# Ger tillbaka ett random ord från en ordlista
def getRandWord():
    import random
    wordList = ["hund", "fisk", "katt", "groda", "mus", "krokodil"]
    randomWord = random.choice(wordList)
    return randomWord

# Hämtar inmata gissning och kollar att det är en tillåten bokstav, att spelet inte är över,
# att bokstaven inte redan är gissad, och därefter kallar den på gissningshanteraren.
def getUserGuess():
    x1 = guessingBox.get()

    # check if character is allowed (inside allowedChars)
    charAllowed = False
    for i in range(len(allowedChars)):
        if x1 == allowedChars[i]:
            charAllowed = True
    if not charAllowed:
        print("Guess is not a valid character")
        return

    # kollar om spelet är avslutat
    if gameInstance.isGameOver():
        print("Game is finished!")
        return

    # Kollar om bokstav redan använd
    charGuessed = False
    for i in range(len(guessedChars)):
        if x1 == guessedChars[i]:
            charGuessed = True
            break
    if charGuessed:
        print("Character already used")
        return
    guessedChars.append(x1)
    showGuessed.config(text=showGuessed.cget("text") + " " + str(x1))
    handleGuess(x1)

# Genererar texten som wordLabel startar med, ser ut enligt _ _ _ _ beroende på hur många bokstäver
def genCoverText():
    text = ""
    for i in range(len(randomWord)):
        text += "_ "
    return text

# Gör likt genCoverText funktionen fast den sätter in korrekt gissade bokstäver på korrekta ställen också,
# t.ex. om man har ordet hund och har gissat u & d så sätter denna funktionen labelns text till: "_ u _ d"
def updateWordTextGUI():
    strText = ""
    for char in textGUI:
        if char == " ":
            strText += "_ "
        else:
            strText += (char + " ")

    wordLabel.config(text=strText)


def handleGuess(guess):
    # För längden av alla bokstäver i orginal ordet så checkar man om gissningen (bokstaven)
    # är korrekt och då tar man bort bokstaven/bokstäverna samt lägger in bokstaven/bokstäverna på
    # rätt plats i texten för GUI.
    correctGuess = False
    for i in range(len(charListOfRandWord)):
        if guess == charListOfRandWord[i]:
            correctGuess = True
            charsLeftToGuess.remove(charListOfRandWord[i])
            textGUI[i] = charListOfRandWord[i]

    # Om det var korrekt bokstav uppdateras GUI så användaren får visuell feedback
    # och sen checkas även om spelet är avslutat via spelklassens funktion isGameOver.
    # Om inkorrekt bokstav så raderas en kroppsdel från kroppsdelslistan samt GUI:et.
    # Det sker även en check som kollar om spelet är över via isGameOver.
    if correctGuess:
        updateWordTextGUI()
        if gameInstance.isGameOver():
            print("You Won!")
    else:
        print("Wrong Guess!")
        if len(bodyParts) > 0:
            bodyPart = bodyParts.pop(0)
            gameInstance.increaseGuesses()
            canvas.delete(bodyPart)
            if gameInstance.isGameOver():
                print("You Lost! The word was: ", randomWord)
        else:
            print("Nothing left to remove!")


# Tar in en sträng och ger tillbaka en lista med varje index motsvarande en bokstav i strängen.
def strToCharList(str):
    charList = []
    for i in range(len(str)):
        charList.append(str[i])
    return charList


window = Tk()
window.geometry("1000x800")
guessingBox = Entry(window, width=40)
guessingBox.place(x=375, y=400)

# width 14 (14 characters wide) to not overlapp with hanging man picture
# wraplength tells label after how units to make a new row
showGuessed = Label(window, text="", width=12, height=10,
                    wraplength=80, borderwidth=2, relief="solid")
showGuessed.place(x=0, y=0)
allowedChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
guessedChars = []

maxGuesses = 6
# Skapar en spelinstans som är den som håller koll på t.ex gissningar och när spelet är över.
gameInstance = Game(maxGuesses)

randomWord = getRandWord()
print("word: " + randomWord)

# en lista som används främst i handleGuess funktionen för att kunna sätta in korrekt gissade bokstäver och sedan
# ge det till GUI:et
textGUI = [" "] * len(randomWord)

# lista av bokstäver från random ordet, ändras inte när man gissar rätt bokstav
charListOfRandWord = strToCharList(randomWord)

# bokstäver som är kvar att gissa, kommer successivt bli tömd av programmet
charsLeftToGuess = charListOfRandWord.copy()

# Labeln som visar text motsvarande bokstäverna i ordet som skall gissas,
# där det såklart är tomt från början enligt t.ex _ _ _ _ men som sedan uppdateras
# med korrekt gissade bokstäver när dessa sker.
coverText = genCoverText()
wordLabel = Label(window, text=coverText, width=15,
                  height=3, font=("Times New Roman", 25))
wordLabel.place(x=415, y=270)

# Gissaknappen
guessingButton = Button(window, text="Gissa!", command=lambda: getUserGuess(
), bg="grey", width=10, height=4)
guessingButton.place(x=280, y=375)

# Kod för hängagubbe gubben i GUI:et
canvas = Canvas(window, width=500, height=260, bg="lightblue")
canvas.pack(pady=30)
baseLine = canvas.create_line(150, 260, 250, 260, width=3)  # base line?
standLine = canvas.create_line(
    200, 260, 200, 48, width=3)  # line that is standing
suppLine = canvas.create_line(200, 98, 258, 40, width=3)  # supporter stand
topLine = canvas.create_line(200, 40, 300, 30, width=3)  # top line of stand
ropeLine = canvas.create_line(300, 40, 300, 70, width=3)  # rope
head = canvas.create_oval(280, 70, 328, 100, width=3)  # head
stomachLine = canvas.create_line(300, 100, 300, 180, width=3)  # stomach
leftHand = canvas.create_line(300, 185, 278, 155, width=3)  # left hand
rightHand = canvas.create_line(300, 185, 330, 155, width=3)  # right hand
leftLeg = canvas.create_line(300, 188, 278, 230, width=3)  # leftleg
rightLeg = canvas.create_line(300, 188, 338, 230, width=3)  # rightLeg

# Listan av kroppsdelar som gradvis raderas efter inkorrekta gissningar.
bodyParts = [rightLeg, leftLeg, stomachLine, rightHand, leftHand, head]

window.mainloop()
