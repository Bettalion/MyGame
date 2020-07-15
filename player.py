print('player')
class Player:
 def __init__(self,name,classt,element,Baselevel):
  self.name=name
  self.classt=classt
  self.element=element
  self.attack=10
  self.health=100#
  self.baselevel=Baselevel
  # items have [level],(amount) and an arbitrary name
  if self.classt=='Mage': 
   self.inventory=['[1] Standard Wand','[2] Fire Ball (x4)']
  if self.classt=='Barbarian':
   self.inventory==['[1] Standard Club','[2] Relentless Rage (x4)']
  if self.classt=='Thief':
   self.inventory=['[1] Standard Dagger','[2] Executioners Malice (x4)']
  if self.classt=='Warrior':
   self.inventory=['[1] Standard Sword','[2] Splintering Shot (x4)']
  self.pets=[]