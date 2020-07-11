from monsters import *
from player import *
from Leaving import *
import time
import StoryFacts as sf

def attack(PLAYER,mon):
 print(f'{mon.name} a {mon.classt} type monster gets ready to fight you!')
 print(f'{PLAYER.name}:\nHealth:{PLAYER.health} Attack:{PLAYER.attack} Class:{PLAYER.classt} Element:{PLAYER.element}')
 print(f'{mon.name}:\nHealth:{mon.health} Attack:{mon.attack} Class:{mon.classt}')
 time.sleep(4)

def story1(PLAYER,MONSTERS):
 mon=random.choice(MONSTERS)
 attack(PLAYER,mon)

def MakeMonsters(BaseLevel):
 if BaseLevel==5:
  BaseLevel=25
 BaseLevel+=10
 Bettasimha=Monster('Bettasimha','Champion',f'The Champion of Battle, King of {sf.Location}',BaseLevel,'You were obliterated from existence')
 Mon1=Monster(sf.mons1,sf.monse1,sf.monsd1,BaseLevel,sf.fin1)
 Mon2=Monster(sf.mons2,sf.monse2,sf.monsd2,BaseLevel,sf.fin2)
 Mon3=Monster(sf.mons3,sf.monse3,sf.monsd3,BaseLevel,sf.fin3)
 Mon4=Monster(sf.mons4,sf.monse4,sf.monsd4,BaseLevel,sf.fin4)
 Mon5=Monster(sf.mons5,sf.monse5,sf.monsd5,BaseLevel,sf.fin5)
 Mon6=Monster(sf.mons6,sf.monse6,sf.monsd6,BaseLevel,sf.fin6)
 Mon7=Monster(sf.mons7,sf.monse7,sf.monsd7,BaseLevel,sf.fin7)
 monsters=[Bettasimha,Mon1,Mon2,Mon3,Mon4,Mon5,Mon6,Mon7]
 return monsters

def main():
 gameName=sf.gameName
 classes=sf.classes
 elements=sf.elemets
 print(f'Welcome to {gameName}')
 name=input('Enter Player name:')
 print(f'The classes available are:{classes}')
 classt=input('Enter prefered Class:').capitalize()
 if classt not in classes:
  print('Invalid class')
  leave('entered the wrong credentials')
 else:
  print(f'The elements available are:{elements}')
  element=input('Enter prefered Element:').capitalize()
  if element not in elements:
   print('Invalid element')
   leave('entered the wrong credentials')
 try:
  PLAYER=Player(name,classt,element)
 except:
  pass
 BaseLevel=input('What level Would you like to play at, we include Easy ->Insane ?(1-5)')
 print(f'\nWelecome {PLAYER.name}\nWe are starting the {gameName} please wait while this happens')
 MONSTERS=MakeMonsters(BaseLevel)
 story1(PLAYER)
if __name__=='__main__':
 # main()

 # testing 
 PLAYER=Player('Testing','Mage','Fire')
 MONSTERS=MakeMonsters(1)
 story1(PLAYER,MONSTERS)