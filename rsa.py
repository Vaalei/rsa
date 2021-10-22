from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from rsaModules import getCryptoPrimes, getKeys, encrypt, decrypt, removeLetters, int2Text, text2Int, modSize
from webbrowser import open_new



# Generate RSA keys
def genRSA(bits):
    p, q = getCryptoPrimes(bits)
    pk, sk, mod = getKeys(p,q)
    return pk, sk, mod

def rgb(rgb):
    # translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb  


def changeEncrypt():
    value = encryptInputField.get("1.0", END)
    if value == None: return
    if chosenType.get() == "Integer":
        try:
            value = int(value)
        except:
            value = removeLetters(value)
        output = encrypt(value, pk, mod)

    elif chosenType.get() == "Text":
        value = text2Int(value)
        output = encrypt(value, pk, mod)
    else:
        return

    encryptOutputField.delete("1.0","end")
    encryptOutputField.insert("1.0", output)

def changeDecrypt():
    value = decryptInputField.get("1.0", END)
    if value == None: return
    try:
        value = int(value)
    except:
        value = removeLetters(value)
    if chosenType.get() == "Text":
        output = decrypt(value, sk, mod)
        output = int2Text(output, modSize(mod))

    elif chosenType.get() == "Integer":
        output = decrypt(value, sk, mod)
    else:
        return

    decryptOutputField.delete("1.0","end")
    decryptOutputField.insert("1.0", output)

def toggleAdvanced():
    if advanced == False:  
        for i in advancedWidgets:
            i[0].grid(column=i[1][0], row=i[1][1])
        advanced = True
    else:
        for i in advancedWidgets:
            i[0].grid_forget()
        
    
    


BGCOLOUR = "#010409"


root = Tk()
#root.geometry("550x230")
root.title("RSA Kryptering @Vaalei")
root.configure(
    background=BGCOLOUR
)
root.iconbitmap("./pictures/main.ico")

style = ttk.Style()
style.theme_use('alt')
style.configure("BW.TLabel", 
    foreground="white", 
    background=BGCOLOUR,
    font= "helvetica 10 bold"
)

style.configure(
    "BW.TButton",
    borderwidth=5,
    border=rgb((20,20,20)),
    background=BGCOLOUR,
    foreground="white",
    font="helvetica 10 bold"
)
style.map('TButton', background=[('active', BGCOLOUR)])

style.configure(
    "Github.TLabel",
    foreground="blue",
    font="Helvetica 11",
    background=BGCOLOUR
)


# ENCRYPTION
# Input
encryptTitle = ttk.Label(root, style="BW.TLabel", text="Encryptor", font="Helvetica 18 bold", padding=0)
encryptTitle.grid(column=1, row=0)

encryptInputText = ttk.Label(root, style="BW.TLabel", text="Input:", padding=0)
encryptInputText.grid(column=0, row=1)

encryptInputField = Text(root, width=30, height=10, font=("Helvetica", 10))
encryptInputField.grid(column=1, row=1)

# Output
encryptOutputText = ttk.Label(root, style="BW.TLabel", text="Encrypted:", padding=0)
encryptOutputText.grid(column=0, row=2)

encryptOutputField = Text(root, width=30, height=10, font=("Helvetica", 10))
encryptOutputField.grid(column=1, row=2)

calculateButton = ttk.Button(root, style="BW.TButton", text="Calculate", padding=5, command=lambda: changeEncrypt(), cursor="hand2")
calculateButton.grid(column=1, row=3)

# END OF ENCRYPTION




# DECRYPTION
# Input
decryptTitle = ttk.Label(root, style="BW.TLabel", text="Decryptor", font="Helvetica 18 bold", padding=0)
decryptTitle.grid(column=4, row=0)
decryptInputText = ttk.Label(root, style="BW.TLabel", text="Input:", padding=0)
decryptInputText.grid(column=3, row=1)

decryptInputField = Text(root, width=30, height=10, font=("Helvetica", 10))
decryptInputField.grid(column=4, row=1)

# Output
decryptOutputText = ttk.Label(root, style="BW.TLabel", text="Encrypted:", padding=40)
decryptOutputText.grid(column=3, row=2)

decryptOutputField = Text(root, width=30, height=10, font=("Helvetica", 10))
decryptOutputField.grid(column=4, row=2)



calculateButton = ttk.Button(root, style="BW.TButton", text="Calculate", padding=5, command=lambda: changeDecrypt(), cursor="hand2")
calculateButton.grid(column=4, row=3)

# END OF DECRYPTION


# OPTIONS
#ttk.Label(root, style="BW.TLabel", text="Type of encryption:", font="Halvetica 10 bold").grid(column=0, row=6)
chosenType = StringVar()
chosenType.set("Integer")
chooseType = ttk.OptionMenu(root, chosenType, "Choose Encryption Type Here", "Integer", "Text")
chooseType.grid(column=1, row=5)
chooseType.configure(
    width=30,
    cursor="hand2", 
    style="BW.TButton"
)

# Advanced
# Show prime numbers, N, E 
showAdvancedButton = ttk.Button(root, style="BW.TButton", text="Toggle advanced", command=lambda: toggleAdvanced())
showAdvancedButton.grid(column=4, row=5)


# PADDING
ttk.Label(root, style="BW.TLabel", text="").grid(column=0, row=4)           # Between converters and below
ttk.Label(root, style="BW.TLabel", text="").grid(column=0, row=98)          # Before Github link
ttk.Label(root, style="BW.TLabel", text="     ").grid(column=99,row=100)    # Make a margin bottom right



# Github
github = ttk.Label(root, style="Github.TLabel", text="Github @Vaalei", cursor="hand2", padding= 10)
github.grid(column=0,row=99)
github.bind("<Button-1>", lambda e: open_new("https://github.com/Vaalei"))


if __name__ == "__main__":
    advanced = False
    pk, sk, mod = genRSA(512)
    root.mainloop()






