from tkinter import *
import pyperclip
import random, string

root = Tk()
root.title('Password Generator')
root.geometry('400x400')
root.resizable(False, False)
root.config(bg='#ffcba4')

heading = Label(root, text='PASSWORD GENERATOR', font=('Times New Roman', 15, 'bold'), bg='#ffcba4').pack()

pass_label = Label(root, text='Password Length', font=('Times New Roman', 15, 'bold'), height=3, width=20, bg='#ffcba4').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=20).pack()

pass_str = StringVar()

def Generator():
    Password = ''
    for x in range(4):
        Password += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        Password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    pass_str.set(Password)

Button(root, text='Generate', font=('Times New Roman', 13), height=2, width=13, command=Generator, bg='#cba4ff').pack(pady=10)
Entry(root, textvariable=pass_str, width=25).pack(pady=10)

def copy_pass():
    pyperclip.copy(pass_str.get())

Button(root, text='Copy to Clipboard', font=('Times New Roman', 13), command=copy_pass, bg='#a4ffcb').pack(pady=10)

root.mainloop()
