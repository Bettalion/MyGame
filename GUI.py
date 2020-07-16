from tkinter import *
import time
import StoryFactsData as sf
import random
from Leaving import *

class GUI:
 def __init__(self,player,mons):
  self.playert=player
  self.mons=mons
 def Homescreen(self):
   Home=Tk()
   Home.title(f'{sf.gameName} - HomeScreen')
   Home.configure(bg='light blue')

   def showstates():
      # % (vars1.get(), vars2.get(),vars3.get(), vars4.get())
    if len(NameE.get()) >=1:
     returnValue=[NameE.get()]
    else:
      returnValue=['NoName']
    cont=[]
    elementssum=(var1.get()+var2.get()+var3.get()+var4.get())
    classsum=(vars1.get()+vars2.get()+vars3.get()+vars4.get())
    difsum=(difl1.get()+difl2.get()+difl3.get()+difl4.get()+difl5.get())
    if classsum > 1 or classsum <=0:
      print('Invalid Class')
      cont.append(False)
      # leave('entered the wrong credentials')
    if elementssum > 1 or elementssum <=0:
      print('Invalid Element')
      cont.append(False)
    if difsum > 1 or difsum <=0:
      print('Invalid Difficulty Level\n')
      cont.append(False)
    if len(cont) == 0:
     if vars1.get() ==1:
      returnValue.append(sf.classes[0])
     if vars2.get() ==1:
      returnValue.append(sf.classes[1])
     if vars3.get() ==1:
      returnValue.append(sf.classes[2])
     if vars4.get() ==1:
      returnValue.append(sf.classes[3])
     if var1.get() ==1:
      returnValue.append(sf.elements[0])
     if var2.get() ==1:
      returnValue.append(sf.elements[1])
     if var3.get() ==1:
      returnValue.append(sf.elements[2])
     if var4.get() ==1:
      returnValue.append(sf.elements[3])
     if difl1.get() ==1:
      returnValue.append(1)
     if difl2.get() ==1:
      returnValue.append(2)
     if difl3.get() ==1:
      returnValue.append(3)
     if difl4.get() ==1:
      returnValue.append(4)
     if difl5.get() ==1:
      returnValue.append(5)
     def closehome():
      Home.destroy()
      self.closewin()
     self.ReturnValueChar=returnValue
     win=Tk()
     self.win=win
     win.title('Confirm')
     Label(win,text=f'The Character you have chosen is:\nNamed: {returnValue[0]}\nClass: {returnValue[1]}  Element: {returnValue[2]}\n\nYou have also chosen difficulty level {returnValue[3]}').grid(column=0,row=0,columnspan=4,rowspan=4)
    #  print(f'The Character you have chosen is:\nNamed: {returnValue[0]}\nClass: {returnValue[2]}  Element: {returnValue[1]}\n\nYou have also chosen difficulty level {returnValue[3]}')
     submitb=Button(win,text='Start Game',padx=18,bg='#b65ee6',command=closehome)
     changeb=Button(win,text='Change Settings',padx=5,bg='#f27f3d',command=self.closewin)
     submitb.grid(row=5,column=1)
     changeb.grid(row=5,column=0)
   
   Label(Home,text=f'Welcome to {sf.gameName}!',bg='light blue',font=("Helvetica Neue", 44)).grid(row=0,column=0,columnspan=8)
   Label(Home,text='A game made by Project Bettalion',bg='light blue',font=("Helvetica Neue", 10,'italic'),pady=25).grid(column=0)
   NameE=Entry(Home,bg='grey')
   NameE.grid(column=1,row=2)
   Label(Home,text='Name:',pady=10,bg='light blue').grid(column=0,row=2)
   Label(Home,text='Prefered Class:',pady=10,bg='light blue').grid(column=0,row=4)
   vars1=IntVar()
   vars2=IntVar()
   vars3=IntVar()
   vars4=IntVar()
   ClassE1=Checkbutton(Home,bg='grey',text=sf.classes[0],variable=vars1)
   ClassE2=Checkbutton(Home,bg='grey',text=sf.classes[1],variable=vars2)
   ClassE3=Checkbutton(Home,bg='grey',text=sf.classes[2],variable=vars3)
   ClassE4=Checkbutton(Home,bg='grey',text=sf.classes[3],variable=vars4)
   ClassE1.grid(column=1,row=4)
   ClassE2.grid(column=2,row=4)
   ClassE3.grid(column=1,row=5)
   ClassE4.grid(column=2,row=5)
   
   var1=IntVar()
   var2=IntVar()
   var3=IntVar()
   var4=IntVar()
   ElementE1=Checkbutton(Home,bg='grey',text=sf.elements[0],variable=var1)
   ElementE2=Checkbutton(Home,bg='grey',text=sf.elements[1],variable=var2)
   ElementE3=Checkbutton(Home,bg='grey',text=sf.elements[2],variable=var3)
   ElementE4=Checkbutton(Home,bg='grey',text=sf.elements[3],variable=var4)
   Label(Home,text='Prefered Element:',pady=10,bg='light blue').grid(column=0,row=6)
   ElementE1.grid(column=1,row=6)
   ElementE2.grid(column=2,row=6)
   ElementE3.grid(column=1,row=7)
   ElementE4.grid(column=2,row=7)
   
   difl1=IntVar()
   difl2=IntVar()
   difl3=IntVar()
   difl4=IntVar()
   difl5=IntVar()
   Label(Home,text='What level Would you like to play at?\n Easy ->Insane(1-5):',pady=25,bg='light blue').grid(column=0,row=8)
   diffl1=Checkbutton(Home,bg='grey',text='1',variable=difl1)
   diffl2=Checkbutton(Home,bg='grey',text='2',variable=difl2)
   diffl3=Checkbutton(Home,bg='grey',text='3',variable=difl3)
   diffl4=Checkbutton(Home,bg='grey',text='4',variable=difl4)
   diffl5=Checkbutton(Home,bg='grey',text='5',variable=difl5)
   diffl1.grid(column=1,row=8)
   diffl2.grid(column=2,row=8)
   diffl3.grid(column=3,row=8)
   diffl4.grid(column=4,row=8)
   diffl5.grid(column=random.randint(2,3),row=9)
   Button(Home,text='Start Game',bg='#f27f3d',command=showstates).grid(row=10,columnspan=4)
   Home.mainloop()
   return self.ReturnValueChar #name,class,ele,diff
 def CapturePet(self,pet):
   win= Tk()
   self.win=win
   self.pet=pet
   win.title('Capture Pet')
   TryB=Button(win,text=f'Try to capture {pet.name}',command=self.CapPet)
   TryB.grid(row=0,column=0,columnspan=2)
   backB=Button(win,text='Back',command=self.returnB)
   backB.grid(row=1,column=0,columnspan=2)
   self.win.mainloop()
 def CapPet(self):
   self.closewin()
   num2find=random.randint(1,self.pet.CapDiff)
   Rnumber=random.randint(1,self.pet.CapDiff)
   print(Rnumber,num2find)
   if Rnumber == num2find:
     capwin=Tk()
     capwin.title('Well done!')
     Label(capwin,text=f'You were able to capture {self.pet.name}\nWell Done',padx=25).grid(row=0,column=0,columnspan=2) 
     choice=input(f'Would you like to change {self.pet.name}\'s name?(Y/N)').upper()
     if choice == 'Y':
       print(f'Enter the new name of {self.pet.name} in the window above. Then exit to continue the game')
       namegetb=Entry(capwin)
       namegetb.grid(row=1,column=0)
       self.namegetb=namegetb
       submitb=Button(capwin,text='Submit',command=self.getName)
       submitb.grid(row=1,column=1)
   else:
     capwin=Tk()
     capwin.title('Unfortunate')
     Label(capwin,text=f'You were unable to capture {self.pet.name}',padx=25).pack()
   capwin.mainloop()
   
 def getName(self):
   NewName=self.namegetb.get()
   print(NewName)
   self.pet.name=NewName
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
    if self.mons.name in sf.Bosses:
     time.sleep(0.25)
     Label(runwin,text='You are not able to run from a Boss!').pack()
    else:
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
     Damage+=5+random.randint(-2,2)
   else:
     Damage+=10
   print(f'It dealt {Damage}!')
   self.mons.health-=Damage
   

   
# gui=GUI('x','z')
# returnValue=gui.Homescreen()
# print(f'The Character you have chosen is:\nNamed: {returnValue[0]}\nClass: {returnValue[2]}  Element: {returnValue[1]}\n\nYou have also chosen difficulty level {returnValue[3]}')
