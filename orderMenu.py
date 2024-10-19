from tkinter import *
#klass över all mat, tar in namn, pris
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#Skapar GUI:et för maten
def draw(food, frame):
    frame = Frame(frame)
    label = Label(frame, text=food.name, width=15, height=1)
    label.pack(side=LEFT)
    priceLabel = Label(frame, text=str(food.price) + "kr", width=15, height=2, borderwidth=1, relief="solid")
    priceLabel.pack(side=LEFT)
    button = Button(frame, text="+",command=lambda: addOrder(food), width=12, height=2, bg="#d6c9b1")
    button.pack(side=RIGHT)
    minusButton = Button(frame, text="-", command=lambda: removeOrder(food), width=12, height=2, bg="#d6c9b1",)
    minusButton.pack(side=RIGHT)
    frame.pack()

#lägger till i GUIorderlist och i den "riktiga" listan
def addOrder(food):
    orderList.insert(orderList.size(), food.name + " " + str(food.price) + "kr")
    orders.append(food)
    updateSum(food)

def removeOrder(food):
    #kollar om maten som skall tas bort är i orders, om inte ignorera
    if orders.count(food) <= 0:
        print(food.name + " not in orderList, can't remove")
        return

    #clears the orderList
    orderList.delete("0", "end")


    #tar bort food instansen från orders (listan med klass instanserna)
    orders.remove(food)
    #fyller upp orderlist från orders
    for i in range(len(orders)):
        orderList.insert(i, orders[i].name + " "  + str(orders[i].price) + "kr")
    updateSum(food)

#uppdaterar summan
def updateSum(food):
    sum = 0
    for i in range(len(orders)):
        sum += orders[i].price
    sumLabel.configure(text="Summa: " + str(sum) + "kr")

#skriver ut kvitto
def printReceipt():
    sum = 0
    print("\n\nBeställning:")
    for i in range(len(orders)):
        print(orders[i].name)
        sum += orders[i].price
    print("\nTotala Pris: " + str(sum) + "kr")

#skapar huvudfönstret
window = Tk()
window.geometry("700x700")
window.title("Restaurang")
window.configure(bg="#fff2cc")
window.resizable(0, 0)
window.configure(cursor="tcross")

orderList = Listbox(window, height="30", width="35", borderwidth=5)
orderList.place(x=0, y=0)
orders = []
receipt = Button(window, text="Beställ", command=lambda: printReceipt(), font=("Times New Roman", 12), borderwidth=2, relief="solid", highlightthickness=1, highlightbackground="black", height="5", width="10")
receipt.place(x=0, y= 550)

sumLabel = Label(window, text="Summa: ", font=("Times New Roman", 12),borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
sumLabel.place(x=0, y=500)

#huvudrätter
Pizza = Food("Pizza", 75)
vegBeef = Food("Veg biff", 100)
Soup = Food("Soppa", 60)
Beef = Food("Biff", 165)

#dryck
Water = Food("Vatten", 45)
CocaCola = Food("Coca-Cola", 55)
Beer = Food("Öl", 95)
Wine = Food("Vin", 100)

#Efterrätt
Pie = Food("Paj", 65)
Icecream = Food("Glass", 55)
Chocolate = Food("Choklad", 30)
Cake = Food("Tårta", 65)

draw(Pizza, window)
draw(vegBeef, window)
draw(Soup, window)
draw(Beef, window)
draw(Water, window)
draw(CocaCola, window)
draw(Beer, window)
draw(Wine, window)
draw(Pie, window)
draw(Icecream, window)
draw(Chocolate, window)
draw(Cake, window)


window.mainloop()
