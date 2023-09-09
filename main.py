from tkinter import *
from PIL import Image, ImageTk
import pybase64
from tkinter import messagebox

window = Tk()
window.title("Secret Notes")
window.minsize(width=400, height=800)

def save_secret_notes():
    title = title_entry.get()
    notes = secret_text.get("1.0", END)
    if title == "" or notes == "" or master_key_entry.get() == "":
        messagebox.showwarning("Warning !","Fill a title and secret notes")
    else:
        secret_text.delete("1.0", END)
        title_entry.delete(0,'end')
        master_key_entry.delete(0,'end')
        if master_key_entry.get() == "brkn":
            notes = notes.encode("ascii")
            notes = pybase64.b64encode(notes)
            notes = notes.decode("ascii")
            with open("mysecret.txt","a") as secretFile:
                secretFile.write(title + "\n")
                secretFile.write(notes)
                secretFile.write("\n")
        else:
            messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again")

def decrypt_notes():
    title = title_entry.get()
    notes = secret_text.get("1.0", END)

    secret_text.delete("1.0", END)
    if master_key_entry.get() == "brkn":
        notes = notes.encode("ascii")
        notes = pybase64.b64decode(notes)
        notes = notes.decode("ascii")
        secret_text.insert(END, notes)
    else:
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again")


image1 = Image.open("secret.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test,width=100,height=80,bg="gray")
label1.image = test

# Position image
label1.place(x=150,y=50)

title_label = Label(text="Enter your title",font=("Arial",12,"bold"))
title_label.place(x=150,y=150)
title_entry = Entry(window,width=40)
title_entry.place(x=90,y=180)
secret_label = Label(text="Enter your secret",font=("Arial",12,"bold"))
secret_label.place(x=140,y=200)
secret_text = Text(window,width=40,height=20)
secret_text.place(x=40,y=235)
master_key_label = Label(text="Enter master key",font=("Arial",12,"bold"))
master_key_label.place(x=130,y=570)
master_key_entry= Entry(window,width=40,show="*")
master_key_entry.place(x=75,y=600)
save_encrypt_button = Button(text="Save & Encrypt",command=save_secret_notes)
save_encrypt_button.place(x=150,y=630)
decrypt_button = Button(text="Decrypt",command=decrypt_notes)
decrypt_button.place(x=170,y=660)
title_entry.focus()
error_label =Label(text="")
error_label.place(x=100,y=700)
window.mainloop()