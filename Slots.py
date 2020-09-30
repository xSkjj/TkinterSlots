from tkinter import *

# window settings ---
icon = r".\assets\icon.ico"
title = "Slots"
minWidth = 400
minHeight = 400
maxWidth = 400
maxHeight = 500
windowWidth = "400"
windowHeight = "400"
offsetx = "200"
offsety = "200"
bgColor = "#202020"

# apply window settings
root = Tk()
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
root["background"] = bgColor


# define functions --
def trySpin(amt):
    try:
        int(amt)
        amtInput["bg"] = "#404040"
    except:
        if amt == "":
            amtInput["bg"] = "#404040"
        else:
            amtInput["bg"] = "#a00000"


# make elements and set their properties
header = Label(root,
               text = "S L O T S",
               font = "Impact 24",
               fg   = "gold",
               bg   = bgColor)

slotsDisplay = Canvas(root,
                      height = 100,
                      bg = "#f0f")
slotsDisplay.create_text(200, 50, text="not yet implemented")

userInputs = Frame(root,
                   bg   = bgColor,
                   pady = 10)

amtInputLabel = Label(userInputs,
                      text = "Amount:",
                      font = "Arial 10 bold",
                      fg   = "white",
                      bg   = bgColor)

amtInput = Entry(userInputs,
                 bg     = "#404040",
                 fg     = "white",
                 relief = FLAT)

spinBtn = Button(userInputs,
                 command = trySpin(amtInput.get()),
                 text    = "spin",
                 font    = "Arial 10 bold",
                 fg      = "#050",
                 bg      = "light green",
                 relief  = FLAT)

# display the elements
header.pack()
slotsDisplay.pack()
userInputs.pack()
amtInputLabel.grid(column=0, row=0, padx=5)
amtInput.grid     (column=1, row=0, padx=5)
spinBtn.grid      (column=2, row=0, padx=5)

# bind event listeners to elements


root.mainloop()
