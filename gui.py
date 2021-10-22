from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from rsaModules import getCryptoPrimes, getKeys, encrypt, decrypt, removeLetters, int2Text, text2Int, modSize
from webbrowser import BackgroundBrowser, open_new





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
    if chosenType.get() == "Integer":
        try:
            value = int(value)
        except:
            value = removeLetters(value)
        output = encrypt(value, pk, mod)

    elif chosenType.get() == "Text":
        value = text2Int(value)
        output = encrypt(value, pk, mod)

    encryptOutputField.delete("1.0","end")
    encryptOutputField.insert("1.0", output)

def changeDecrypt():
    value = decryptInputField.get("1.0", END)
    try:
        value = int(value)
    except:
        value = removeLetters(value)
    if chosenType.get() == "Text":
        output = decrypt(value, sk, mod)
        output = int2Text(output, modSize(mod))

    elif chosenType.get() == "Integer":
        output = decrypt(value, sk, mod)

    decryptOutputField.delete("1.0","end")
    decryptOutputField.insert("1.0", output)


BGCOLOUR = rgb((18,18,18))


root = Tk()
#root.geometry("550x230")
root.title("RSA Kryptering @Vaalei")
root.configure(
    background=BGCOLOUR
)

frm = ttk.Frame(root, padding=20)
frm.grid()


style = ttk.Style()
style.configure("BW.TLabel", 
    foreground="white", 
    background=BGCOLOUR,
    font= "helvetica 10 bold"
    )




# ENCRYPTION
# Input
encryptTitle = ttk.Label(root, style="BW.TLabel", text="Encrypt", font="Helvetica 18 bold", padding=0)
encryptTitle.grid(column=1, row=0)

encryptInputText = ttk.Label(root, style="BW.TLabel", text="Input:", padding=0)
encryptInputText.grid(column=0, row=1)
encryptInputVar = StringVar()
encryptInputField = Text(root, width=30, height=10)
encryptInputField.grid(column=1, row=1)

# Output
encryptOutputText = ttk.Label(root, style="BW.TLabel", text="Encrypted:", padding=0)
encryptOutputText.grid(column=0, row=2)
encryptOutputVar = StringVar()
encryptOutputField = Text(root, width=30, height=10)
encryptOutputField.grid(column=1, row=2)

calculateButton = ttk.Button(root, style="BW.TLabel", text="Calculate", padding=0, command=lambda: changeEncrypt())
calculateButton.grid(column=1, row=3)

# END OF ENCRYPTION




# DECRYPTION
# Input
decryptTitle = ttk.Label(root, style="BW.TLabel", text="Decrypt", font="Helvetica 18 bold", padding=0)
decryptTitle.grid(column=4, row=0)
decryptInputText = ttk.Label(root, style="BW.TLabel", text="Input:", padding=0)
decryptInputText.grid(column=3, row=1)
decryptInputVar = StringVar()
decryptInputField = Text(root, width=30, height=10)
decryptInputField.grid(column=4, row=1)

# Output
decryptOutputText = ttk.Label(root, style="BW.TLabel", text="Encrypted:", padding=40)
decryptOutputText.grid(column=3, row=2)
decryptOutputVar = StringVar()
decryptOutputField = Text(root, width=30, height=10)
decryptOutputField.grid(column=4, row=2)

calculateButton = ttk.Button(root, style="BW.TLabel", text="Calculate", padding=0, command=lambda: changeDecrypt(), cursor="hand2")
calculateButton.grid(column=4, row=3)

# END OF DECRYPTION


# Options
ttk.Label(root, style="BW.TLabel", text="Type of encryption:", font="Halvetica 10 bold").grid(column=0, row=6)
chosenType = StringVar()
chosenType.set("Integer")
chooseType = ttk.OptionMenu(root, chosenType, "Choose Encryption Type Here", "Integer", "Text")
chooseType.grid(column=1, row=6)
chooseType.configure(
    width=30
)


# PADDING
#ttk.Label(root, style="BW.TLabel", text="", padding=0).grid(column=2,row=99) # Between different convertors
ttk.Label(root, style="BW.TLabel", text="").grid(column=0, row=4) # Between 
ttk.Label(root, style="BW.TLabel", text="").grid(column=0, row=98) # Before Github link
ttk.Label(root, style="BW.TLabel", text="     ").grid(column=99,row=100)


# Github
github = Label(root, text="Github.com @Vaalei", fg="blue", cursor="hand2", font="Helvetica 11", bg=BGCOLOUR)
github.grid(column=0,row=99)
github.bind("<Button-1>", lambda e: open_new("https://github.com/Vaalei"))


if __name__ == "__main__":
    pk, sk, mod = genRSA(256)
    root.mainloop()