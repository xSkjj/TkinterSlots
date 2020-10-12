import tkinter as tk


# apply window settings
root = tk.Tk()
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
root["background"] = bgColor


# make elements and set their properties
header = tk.Label(root,
               text = "S  L  O  T  S",
               font = "Impact 24",
               fg   = "gold",
               bg   = bgColor)

slotsDisplay = tk.Canvas(root,
                      width              = 302,
                      height             = 100,
                      bg                 = "#c3a469",
                      highlightthickness = 2)
sDw = int(slotsDisplay["width"])
sDh = int(slotsDisplay["height"])
slotsDisplay.create_line(sDw / 3,   0, sDw / 3,     sDh + 4, fill="white")
slotsDisplay.create_line(sDw / 3*2, 0, sDw / 3 * 2, sDh + 4, fill="white")
slotsDisplay.create_text(sDw/6-1,   sDh / 2, text="$", font="Consolas 32", fill="white", tags="symA")
slotsDisplay.create_text(sDw*0.5,   sDh / 2, text="$", font="Consolas 32", fill="white", tags="symB")
slotsDisplay.create_text(sDw/1.2+1, sDh / 2, text="$", font="Consolas 32", fill="white", tags="symC")

output = tk.Label(root,
               text = "How much credits would you like to use?",
               font = "Arial 10 bold",
               fg   = "white",
               bg   = "black")

userInputs = tk.Frame(root,
                   bg = bgColor)

amtInputLabel = tk.Label(userInputs,
                      text = "Amount:",
                      font = "Arial 10 bold",
                      fg   = "white",
                      bg   = bgColor)

amtInput = tk.Entry(userInputs,
                 bg               = "#404040",
                 insertbackground = "white",
                 fg               = "white",
                 relief           = "flat")

spinBtn = tk.Button(userInputs,
                 command = trySpin,
                 text    = "spin",
                 font    = "Arial 10 bold",
                 fg      = "#050",
                 bg      = "light green",
                 relief  = "flat")

balLabel = tk.Label(root,
                 text = f"Balance: {bal}",
                 font = "Arial 10 bold",
                 fg   = "gold",
                 bg   = bgColor)

# display the elements
header.pack()
slotsDisplay.pack(pady=4)
output.pack(fill=X, padx=8, pady=(24, 4))
userInputs.pack()
amtInputLabel.grid(column=0, row=0, padx=5)
amtInput.grid     (column=1, row=0, padx=5)
spinBtn.grid      (column=2, row=0, padx=5)
amtInput.insert(0, "0")
balLabel.pack()


root.mainloop()
