from tkinter import *
import time
import StoryFactsData as sf
import random

class GUI:
 def __init__(self,player,mons):
  self.playert=player
  self.mons=mons
 def closewin(self):
   self.win.destroy()
 def returnB(self):
   self.win.destroy()
   self.options()
 def GetAttacks(self):
   if self.playert.classt == 'Mage':
    Attacks=sf.MageAttacks()
   if self.playert.classt == 'Thief':
    Attacks=sf.ThiefAttacks()
   if self.playert.classt == 'Barbarian':
    Attacks=sf.BarbarianAttacks()
   if self.playert.classt == 'Warrior':
    Attacks=sf.WarriorAttacks()
   self.attacks=Attacks
 def DamageDelt(self,BaseDamage):
   Damage=BaseDamage
   if self.mons.classt == self.playert.classt:
     Damage+=BaseDamage*0.5
   return Damage
 def l1A(self):
   print(f'You attacked {self.mons.name} with {self.attacks[0]}, it caused {self.DamageDelt(self.attacks[1])} damage')
   self.mons.health-=self.DamageDelt(self.attacks[1])
   self.closewin()
  #  \/ gives a chance to have another attack
   chance=random.randint(1,100) 
   if chance==84:
    self.attack(True)
 def l2A(self):
   print(f'You attacked {self.mons.name} with {self.attacks[2]}, it caused {self.DamageDelt(self.attacks[3])} damage')
   self.mons.health-=self.DamageDelt(self.attacks[3])
   self.closewin()
   chance=random.randint(1,100)
   if chance in sf.chance:
    self.attack(True)
 def H1A(self):
   print(f'You attacked {self.mons.name} with {self.attacks[4]}, it caused {self.DamageDelt(self.attacks[5])} damage')
   self.mons.health-=self.DamageDelt(self.attacks[5])
   self.closewin()
 def H2A(self):
   print(f'You attacked {self.mons.name} with {self.attacks[6]}, it caused {self.DamageDelt(self.attacks[7])} damage')
   self.mons.health-=self.DamageDelt(self.attacks[7])
   self.closewin()

 def options(self):
  win= Tk()
  self.win=win
  win.title('Options')
  attackb=Button(win,text='Attack',command=self.attack)
  attackb.grid(row=0,column=0)
  itemb=Button(win,text='Items',command=self.Items)
  itemb.grid(row=0,column=1)
  attackb=Button(win,text='Run',command=self.Run)
  attackb.grid(row=1,column=0)
  itemb=Button(win,text='Pets')
  itemb.grid(row=1,column=1)
  win.mainloop()
 def attack(self,M=FALSE):#M is the possibility to return, determined by heavy or light attacks
  if M==False:
    self.closewin()
  win= Tk()
  self.win=win
  win.title('Attack')

  self.GetAttacks()
  l1B=Button(win,text=self.attacks[0],command=self.l1A)
  l1B.grid(row=0,column=0)
  l2B=Button(win,text=self.attacks[2],command=self.l2A)
  l2B.grid(row=0,column=1)
  H1B=Button(win,text=self.attacks[4],command=self.H1A)
  H1B.grid(row=1,column=0)
  H2B=Button(win,text=self.attacks[6],command=self.H2A)
  H2B.grid(row=1,column=1)
  if M==False:
    backB=Button(win,text='Back',command=self.returnB)
    backB.grid(row=2,column=0,columnspan=2)
  win.mainloop()
 def Items(self):
   self.closewin()
   win= Tk()
   self.win=win
   win.title('Items/Bag')
   backB=Button(win,text='Back',command=self.returnB)
   backB.grid(row=0,column=0,columnspan=2)
   for item in self.playert.inventory:
     itemB=Button(win,text=item)
     itemB.config(command=lambda button=itemB: self.itemChosen(button))
     itemB.grid()
   win.mainloop()
 def Run(self):
   self.closewin()
   win= Tk()
   self.win=win
   win.title('Run')
   
   backB=Button(win,text='Back',command=self.returnB,padx=10)
   backB.grid(row=0,column=0,columnspan=2)
   chance=random.randint(1,100)
   self.chance2run=chance
   runB=Button(win,text='Try to Run?',command=self.Runnable,padx=45,pady=10)
   runB.grid(row=1,column=1,rowspan=2)
   
   
   win.mainloop()
 def Runnable(self):
    runwin=Tk()
    runwin.title('Can You Run?')
  #  if self.mons.name in sf.Bosses:
  #    Label(runwin,text='You are not able to run from a Boss!').pack()
  #    time.sleep(1.5)
  #  else:
    self.closewin()
    if self.chance2run in sf.chance:
      time.sleep(random.randint(0,3))
      Label(runwin,text='You were able to Run!',padx=5).pack()
    else:
      time.sleep(random.randint(0,2))
      Label(runwin,text='You were not able to Run!',padx=5).pack()
    time.sleep(random.randint(1,3))
    runwin.mainloop()
    runwin.destroy()
 def itemChosen(self,button):
   ChosenItem=button['text']
   try:
    ItemStem=ChosenItem.split('(')[0]
    numofitemso=ChosenItem.split('(x')[1].split(')')[0]
    item2=ChosenItem.split(')')[1]
    numofitemsn=int(numofitemso)-1
    if numofitemsn>=0:
      if ItemStem in sf.AvailableItems:
        NewItem=ItemStem+'(x'+str(numofitemsn)+')'+item2
        self.playert.inventory.append(NewItem)
        self.playert.inventory.remove(ChosenItem)
        self.ItemLauncher(ItemStem,0)
   except:
     if ChosenItem in sf.AvailableItems:
       self.ItemLauncher(ChosenItem,1)
   self.closewin()
 def ItemLauncher(self,ChosenItem,Type):
   print(f'You used {ChosenItem} on {self.mons.name}!')
   Level=ChosenItem.split('[')[1].split(']')[0]
   Damage=int(Level)*10
   if Level=='5':
     Damage=75
   if Type==1:
     Damage+=5
   else:
     Damage+=10
   print(f'It dealt {Damage}!')
   self.mons.health-=Damage
   

   
   
# x=player()
# s=player()
# now=GUI(x,s)
# now.options()
