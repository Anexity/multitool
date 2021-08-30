# multitool

import clipboard
import tkinter as tk
import tkinter.messagebox
import random
import subprocess

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

# ipcheck input side - lit
iptex1 = tk.Label(
    text="target ip",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)

ipe1 = tk.Entry(
    fg="white",
    bg="#171717",
    width=30
)

iptex2 = tk.Label(
    text="port start",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)

ipe2 = tk.Entry(
    fg="white",
    bg="#171717",
    width=30
)

iptex3 = tk.Label(
    text="port end",
    fg="white",
    bg="#171717",
    width=26,
    height=2
)

ipe3 = tk.Entry(
    fg="white",
    bg="#171717",
    width=30
)

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

# ip checker

button3 = tk.Button(
    text="check ip",
    width=25,
    height=3,
    bg="#999999",
    fg="#171717",
)

def handle_click3(event):
    webvar = (ipe1.get())
    if(webvar != ""):
        for ping in range(int(ipe2.get()), int(ipe3.get())):
            adress = (webvar) + ":" + str(ping)
            res = subprocess.call(['ping', adress])
            if res == 0:
                tkinter.messagebox.showinfo(
                    title=("ping process"),
                    message=("a ping went through to host.")
                )
            elif res == 2:
                tkinter.messagebox.showerror(
                    title=("ping process"),
                    message=("no response was recieved.")
                    )
            else:
                tkinter.messagebox.showerror(
                    title=("ping process"),
                    message=("pinging the host failed.")
                )

# packing all the windows

greeting.pack()
input1.pack()
e1.pack()
input2.pack()
e2.pack()
button1.bind("<Button-1>", handle_click)
button2.bind("<Button-1>", handle_click2)
button1.pack()
button2.pack()
iptex1.pack()
ipe1.pack()
iptex2.pack()
ipe2.pack()
iptex3.pack()
ipe3.pack()
button3.bind("<Button-1>", handle_click3)
button3.pack()

window.mainloop()
