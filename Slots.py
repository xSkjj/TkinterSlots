from tkinter import *

# window settings
icon = r".\assets\icon.ico" # icon in the top left corner
title = "Slots"             # Title at the top of the window
minWidth = 400              # minimum width you can resize the window to
minHeight = 400             # minimum height you can resize the window to
maxWidth = 400              # maximum width you can resize the window to
maxHeight = 500             # maximum height you can resize the window to
windowWidth = "400"         # the width of the window when starting
windowHeight = "400"        # the height of the window when starting
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
    try:
        int(amt)
        amtInput.configure(bg = "#404040")
        print(amt)
    except:
        if amt == "":
            amtInput.configure(bg = "#404040")
            print(amt)
        else:
            amtInput.configure(bg = "#a00000")
            print(amt)



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
slotsDisplay.pack()
userInputs.pack()
amtInputLabel.grid(column=0, row=0, padx=5)
amtInput.grid     (column=1, row=0, padx=5)
spinBtn.grid      (column=2, row=0, padx=5)
amtInput.insert(0, "0")

# bind event listeners to elements
# None


root.mainloop()
