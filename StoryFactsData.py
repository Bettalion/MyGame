import random
from monsters import *
Location='Location'
# Monster(1,2,3,4)
gameName='Game'
classes=['Mage','Warrior','Barbarian','Thief']
elements=['Fire','Water','Earth','Wind']
# monsters: name,element,description,finishing move
mons1,monse1,monsd1,fin1 ='Mons1','Fire','description of mons1','you were killed'
mons2,monse2,monsd2,fin2 ='Mons2','water','description of mons2','you were killed'
mons3,monse3,monsd3,fin3 ='Mons3','Fire','description of mons3','you were killed'
mons4,monse4,monsd4,fin4 ='Mons4','water','description of mons4','you were killed'
mons5,monse5,monsd5,fin5 ='Mons5','wind','description of mons5','you were killed'
mons6,monse6,monsd6,fin6 ='Mons6','earth','description of mons6','you were killed'
mons7,monse7,monsd7,fin7 ='Mons7','water','description of mons7','you were killed'
Bosses=['Bettasimha',mons1,mons2,mons3,mons4,mons5,mons6,mons7]
# player attacks:
# Mage:
def MageAttacks():
 mal1n,mal1d,mal2n,mal2d,mah1n,mah1d,mah2n,mah2d = 'mage light 1',7,'mage light 2',7,'mage heavy 1',10,'mage heavy 2',10
 return [mal1n,mal1d,mal2n,mal2d,mah1n,mah1d,mah2n,mah2d]
# barbarian:
def BarbarianAttacks():
 bal1n,bal1d,bal2n,bal2d,bah1n,bah1d,bah2n,bah2d = 'bar light 1',7,'bar light 2',7,'bar heavy 1',10,'bar heavy 2',10
 return[bal1n,bal1d,bal2n,bal2d,bah1n,bah1d,bah2n,bah2d]
# thief:
def ThiefAttacks():
 tal1n,tal1d,tal2n,tal2d,tah1n,tah1d,tah2n,tah2d = 'thief light 1',7,'thief light 2',7,'thief heavy 1',10,'thief heavy 2',10
 return [tal1n,tal1d,tal2n,tal2d,tah1n,tah1d,tah2n,tah2d]
# warrior:
def WarriorAttacks():
 wal1n,wal1d,wal2n,wal2d,wah1n,wah1d,wah2n,wah2d = 'war light 1',7,'war light 2',7,'war heavy 1',10,'war heavy 2',10
 return [wal1n,wal1d,wal2n,wal2d,wah1n,wah1d,wah2n,wah2d]

# Items:
AvailableItems=['[1] Standard Wand','[2] Fire Ball ','[1] Standard Club','[2] Relentless Rage ','[1] Standard Dagger','[2] Executioners Malice ','[1] Standard Sword','[2] Splintering Shot ']

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','o','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Chance  (light,run)
chance=[84,4,108]
