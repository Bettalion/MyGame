print('mons')
import random
import StoryFactsData as sf
class Monster:
 def __init__(self,name,element,description,BaseLevel,finnishing=''):
  #classt is the class it is weak against.
  self.name=name
  self.classt=random.choice(sf.classes)
  self.element=element
  self.desc=description
  self.finish=finnishing
  self.BaseLevel=BaseLevel
  # \/ arbitrary values
  self.attack=(7 + (BaseLevel))//2
  self.health=5*BaseLevel
  if self.name in sf.Bosses:
   self.health+=50
  if self.name=='Bettasimha':
   self.classt='Champion'
   self.health+=1000
   self.attack+=100
 def regenerate(self):
   if self.name in sf.Bosses:
    self.health+=50
   self.attack=7 + (self.BaseLevel)
   self.health=5*self.BaseLevel
   if self.name=='Bettasimha':
    self.classt='Champion'
    self.health+=1500
    self.attack+=150
