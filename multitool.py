# multitool start
import clipboard
import tkinter as tk
import tkinter.messagebox
import random

window = tk.Tk()

# greeting label at the top

input1 = tk.Label(
    text="password length",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)

e1 = tk.Entry(
    fg="white",
    bg="#171717",
    width=30
)

input2 = tk.Label(
    text="dice size",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)

e2 = tk.Entry(
    fg="white",
    bg="#171717",
    width=30
)

greeting = tk.Label(
    text="generators",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)
greeting.pack()

# pwgen button & pwgen code modded and copied from my
# original pwgen.

button1 = tk.Button(
    text="Password Generator",
    width=25,
    height=3,
    bg="#999999",
    fg="#171717",
)

def handle_click(event):
    import string

    # printing digits per henrik stackoverflow

    generatorval = int(e1.get())

    SpecialChars = "!@%/()=?+#$&=-"

    password = ""

    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice(SpecialChars)

    for i in range(0, generatorval):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + SpecialChars)

        password = ''.join(random.sample(password, len(password)))

    clipboard.copy(password)


button2 = tk.Button(
    text="diceroll",
    width=25,
    height=3,
    bg="#999999",
    fg="#171717",
)


# Dicethrow button and build with
# random randint.

def handle_click2(event):
    throw1 = random.randint(1, int(e2.get()))

    greeting3 = tkinter.messagebox.showinfo(
        title=("Diceroll"),
        message=(throw1),
    )


input1.pack()
e1.pack()
input2.pack()
e2.pack()
button1.bind("<Button-1>", handle_click)
button2.bind("<Button-1>", handle_click2)
button1.pack()
button2.pack()
window.mainloop()
