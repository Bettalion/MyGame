from monsters import *
from player import *
from Leaving import *
import time

def play(PLAYER):
 print('started')
 

def main():
 gameName='Game'
 classes=['Mage','Warrior','Barbarion','Thief']
 elements=['Fire','Water','Earth','Wind']
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
 print(f'Welecome {PLAYER.name}\nWe are starting the {gameName} please wait while this happens')
 play(PLAYER)

if __name__=='__main__':
 # main()
 PLAYER=Player('Testing','Mage','Fire')
 play(PLAYER)