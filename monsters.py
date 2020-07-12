print('mons')
import random
import StoryFactsData as sf
class Monster:
 def __init__(self,name,element,description,BaseLevel,finnishing=''):
  #classt is the class it is weak against.
  self.name=name
  self.classt=random.choice(sf.classes)
  self.element=element
  if self.name=='Bettasimha':
   self.classt='Champion'
  self.desc=description
  self.finish=finnishing
  # \/ arbitrary values
  self.attack=7 + (BaseLevel)
  self.health=5*BaseLevel
