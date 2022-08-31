import tkinter

import translators as ts
import random
from tkinter import *
import tkinter.messagebox
from libretranslatepy import LibreTranslateAPI

kz= str(random.choice(open("kz.txt").read().split()))


new_Word =False


langChoice=kz






class Window(Frame):

     langChoice = ()

     def __init__(self, master=None):

          Frame.__init__(self, master)
          self.master = master

          # widget can take all window
          self.pack(fill=BOTH, expand=1)


          l = Label(self, text=kz)
          l.config(font=("Courier", 14))
          l.pack()




          randWordBtn= Button(self, text="Translation/Defintion", command=self.onClick)
          randWordBtn.place(x=0,y=0)
          randWordBtn.pack()

          langbutton = Button(self, text="Save to excel", command=self.onClick)
          langbutton.place(x=0, y=0)
          langbutton.pack()
          langChoice=kz

         

          # create button, link it to clickExitButton()
          exitButton = Button(self, text="Exit", command=self.clickExitButton)

          # place button at (0,0)
          exitButton.pack()



     def clickExitButton(self):
          exit()

     def onClick(self):
          if langChoice==kz:

               tkinter.messagebox.showinfo("Definition",(ts.google(kz, from_language='kk',to_language='en')))








root = Tk()


app = Window(root)
root.wm_title("Kazakh Word of The Day")
root.geometry("320x200")
root.mainloop()































