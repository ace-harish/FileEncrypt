__author__ = 'KH9071'

import tkFileDialog
import tkMessageBox
path = ""
l2 = ""
key = "mypersonal"

from Tkinter import *
import EncryptDecrypt

def StartProcess(choice, path, key):
    print "started"
    if choice == "encrypt":
        EncryptDecrypt.encrypt(path,key)
    else:
        EncryptDecrypt.decrypt(path, key)
    tkMessageBox.showinfo('Success','Done!!! You can now check ur file')


def askopenfile():
    global path
    path = tkFileDialog.askopenfilename()
    print path
    global l2
    l2['text'] = path
    tkMessageBox.showinfo('Success','Now please click on Encrypt or Decrypt')

def EncClick():
    global path
    global key
    StartProcess("encrypt",path,key)
    print path

def DecClick():
    global path
    global key
    StartProcess("decrypt",path,key)
    print path


def main():
    root = Tk()

    root.title('Encrypt Decrypt Tool')
    frame_1 = Frame(root,  height=500, width=1000,bg = '#F9F3F4')


    t = Button(root,text='Browse', font=("Maiandra GD", 15), command=askopenfile)
    t.place(x = 100,y = 100)
    global l2
    l1 = Label(root,text = "Key",font=("Maiandra GD", 18),bg = '#F9F3F4')
    l1.place(x = 100,y = 175)

    l2 = Label(root,text = "",font=("Maiandra GD", 15),bg = '#F9F3F4')
    l2.place(x = 200,y = 110)
    keyText = Entry(root,width = 15,font=("Maiandra GD", 18))
    keyText.config(show = "*")
    keyText.place(x=220,y=175)
    d = Button(root,text='Decrypt', font=("Maiandra GD", 15), command=DecClick)
    d.place(x = 100,y = 300)
    c = Button(root,text='Encrypt', font=("Maiandra GD", 15), command=EncClick)
    c.place(x = 300,y = 300)

    frame_1.pack()
    mainloop()

main()
