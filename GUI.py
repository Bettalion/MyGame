from tkinter import *
import time
class GUI:
 def __init__(self):
  pass
 def options(self):
  win= Tk()
  self.win=win
  win.title('Options')
  attackb=Button(win,text='Attack',command=self.attack)
  attackb.grid(row=0,column=0)
  itemb=Button(win,text='Items')
  itemb.grid(row=0,column=1)
  attackb=Button(win,text='Attack')
  attackb.grid(row=1,column=0)
  itemb=Button(win,text='Items')
  itemb.grid(row=1,column=1)
  win.mainloop()
 def attack(self):
  print('You chose attack')
  time.sleep(5)
  self.win.destroy()
  win= Tk()
  self.win=win
  win.title('Attack')
  attackb=Button(win,text='Attack',command=self.attack)
  attackb.grid(row=0,column=0)
  win.mainloop()

now=GUI()
now.options()