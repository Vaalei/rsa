
from tkinter import *
from tkinter import ttk
from rsaModules import getCryptoPrimes, getE, encrypt, decrypt, removeLetters, int2Text, text2Int


# Generate RSA keys
p, q = getCryptoPrimes(256)
n = p*q
pk, sk, mod = getE(p,q)

print("E:", pk, "\nN:", mod, "\n")

# 
def changeEncrypt(value):
    if chosenType.get() == "Integer":
        try:
            value = int(value)
        except:
            value = removeLetters(value)
        output = encrypt(value, pk, mod)
        encryptOutputVar.set(output)

    elif chosenType.get() == "Text":
        value = text2Int(value)
        output = encrypt(value, pk, mod)
        encryptOutputVar.set(output)

def changeDecrypt(value):
    try:
        value = int(value)
    except:
        value = removeLetters(value)
    if chosenType.get() == "Text":
        output = decrypt(value, sk, mod)
        output = int2Text(output, mod)
        decryptOutputVar.set(output)

    elif chosenType.get() == "Integer":
        output = decrypt(value, sk, mod)
        decryptOutputVar.set(output)




# 
root = Tk()
root.geometry("500x200")
root.title("RSA Kryptering @Vaalei")

frm = ttk.Frame(root, padding=20)
frm.grid()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")


"""
frm.grid(row=0, column=0, sticky="NESW")
frm.grid_rowconfigure(0, weight=1)
frm.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
"""

# ENCRYPTION
# Input
ttk.Label(frm, text="Encrypt", font="Helvetica 18 bold", padding=0).grid(column=1, row=0)
encryptInputText = ttk.Label(frm, text="Input:", padding=0).grid(column=0, row=1)
encryptInputVar = StringVar()
encryptInputField = ttk.Entry(frm, textvariable=encryptInputVar).grid(column=1, row=1)

# Output
encryptOutputText = ttk.Label(frm, text="Encrypted:", padding=0).grid(column=0, row=2)
encryptOutputVar = StringVar()
encryptOutputField = ttk.Entry(frm, textvariable=encryptOutputVar).grid(column=1, row=2)

calculateButton = ttk.Button(frm, text="Calculate", padding=0, command=lambda: changeEncrypt(encryptInputVar.get())).grid(column=1, row=3)

# END OF ENCRYPTION

# PADDING
ttk.Label(frm, text="         ").grid(column=2,row=0)
ttk.Label(frm, text=""). grid(column=0, row=4)


# DECRYPTION
# Input
ttk.Label(frm, text="Decrypt", font="Helvetica 18 bold", padding=0).grid(column=4, row=0)
decryptInputText = ttk.Label(frm, text="Input:", padding=0).grid(column=3, row=1)
decryptInputVar = StringVar()
eecryptInputField = ttk.Entry(frm, textvariable=decryptInputVar).grid(column=4, row=1)

# Output
decryptOutputText = ttk.Label(frm, text="Encrypted:", padding=0).grid(column=3, row=2)
decryptOutputVar = StringVar()
decryptOutputField = ttk.Entry(frm, textvariable=decryptOutputVar).grid(column=4, row=2)

calculateButton = ttk.Button(frm, text="Calculate", padding=0, command=lambda: changeDecrypt(decryptInputVar.get())).grid(column=4, row=3)

# END OF DECTRYPTION

# Options
ttk.Label(frm, text="Type of encryption:").grid(column=0, row=6)
chosenType = StringVar()
chosenType.set("Integer")
chooseType = ttk.OptionMenu(frm, chosenType, "Choose Type Here","Integer", "Text").grid(column=1, row=6)



root.mainloop()