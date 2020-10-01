from tkinter import *

# window settings
icon = r".\assets\icon.ico" # icon in the top left corner
title = "Slots"             # Title at the top of the window
minWidth = 400              # minimum width you can resize the window to
minHeight = 250             # minimum height you can resize the window to
maxWidth = 400              # maximum width you can resize the window to
maxHeight = 250             # maximum height you can resize the window to
windowWidth = "400"         # the width of the window when starting
windowHeight = "250"        # the height of the window when starting
offsetx = "200"             # distance between the window's and screen's left edge
offsety = "200"             # distance between the window's and screen's top edge
bgColor = "#202020"         # background color of the window

# apply window settings
root = Tk()
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
root["background"] = bgColor



# define functions
def trySpin():
    amt = amtInput.get()
    #try:
    int(amt)
    amtInput["bg"] = "#404040"
    slots(int(amt))
    #except:
    #    amtInput["bg"] = "#b00000"
    #    if amt == "":
    #        output["text"] = "Amount is empty"
    #    else:
    #        output["text"] = "Amount is not a valid number"

# slots function
bal = 1000
def slots(amt):
    output["text"] = "spinning..."
    global bal
    
    if amt > bal:
        amtInput["bg"] = "#b00000"
        output["text"] = "You don't have enough credits."
        return

    from random import randint
    from time import sleep
    
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]
    
    bal -= amt

    IDsymA = slotsDisplay.find_withtag("symA")[0]
    IDsymB = slotsDisplay.find_withtag("symB")[0]
    IDsymC = slotsDisplay.find_withtag("symC")[0]

    for i in range(0, randint(12, 15)):
        symA = symB = symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymA, text=symA)
        slotsDisplay.itemconfigure(IDsymB, text=symB)
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        sleep(0.1)
    for i in range(0, randint(12, 15)):
        symB = symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymB, text=symB)
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        sleep(0.1)
    for i in range(0, randint(12, 15)):
        symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        sleep(0.1)
    sleep(1)

    if symA == symB and symB == symC:
        bal += amt*100
        output["text"] = "You spent {} and won {} !!!".format(amt, amt*100)
    elif symA == symB or symA == symC or symB == symC:
        bal += amt*3
        output["text"] = "You spent {} and won {} !".format(amt, amt*3)
    else:
        output["text"] = "You spent {} and lost everything.".format(amt)


# make elements and set their properties
header = Label(root,
               text = "S L O T S",
               font = "Impact 24",
               fg   = "gold",
               bg   = bgColor)

slotsDisplay = Canvas(root,
                      width              = 302,
                      height             = 100,
                      bg                 = "#c3a469",
                      highlightthickness = 2)
sDw   = int(slotsDisplay["width"])
sDh   = int(slotsDisplay["height"])
slotsDisplay.create_line(sDw / 3,   0, sDw / 3,     sDh + 4, fill="white")
slotsDisplay.create_line(sDw / 3*2, 0, sDw / 3 * 2, sDh + 4, fill="white")
slotsDisplay.create_text(sDw/6-1,   sDh / 2, text="$", font="Consolas 32", fill="white", tags="symA")
slotsDisplay.create_text(sDw*0.5,   sDh / 2, text="$", font="Consolas 32", fill="white", tags="symB")
slotsDisplay.create_text(sDw/1.2+1, sDh / 2, text="$", font="Consolas 32", fill="white", tags="symC")

output = Label(root,
               text = "How much credits would you like to use?",
               font = "Arial 10 bold",
               fg   = "white",
               bg   = "black")

userInputs = Frame(root,
                   bg   = bgColor)

amtInputLabel = Label(userInputs,
                      text = "Amount:",
                      font = "Arial 10 bold",
                      fg   = "white",
                      bg   = bgColor)

amtInput = Entry(userInputs,
                 bg               = "#404040",
                 insertbackground = "white",
                 fg               = "white",
                 relief           = FLAT)

spinBtn = Button(userInputs,
                 command = trySpin,
                 text    = "spin",
                 font    = "Arial 10 bold",
                 fg      = "#050",
                 bg      = "light green",
                 relief  = FLAT)

# display the elements
header.pack()
slotsDisplay.pack(pady=4)
output.pack(fill=X, padx=8, pady=(24, 4))
userInputs.pack()
amtInputLabel.grid(column=0, row=0, padx=5)
amtInput.grid     (column=1, row=0, padx=5)
spinBtn.grid      (column=2, row=0, padx=5)
amtInput.insert(0, "0")

# bind event listeners to elements
# None


root.mainloop()