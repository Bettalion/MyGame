print('mons')
import random
import StoryFacts as sf
class Monster:
 def __init__(self,name,element,description,BaseLevel,finnishing=''):
  #element is the class it is weak against.
  self.name=name
  self.classt=random.choice(sf.classes)
  self.element=element
  if self.name=='Bettasimha':
   self.element=None
  self.desc=description
  self.finish=finnishing
  # \/ arbitrary values
  self.attack=10 + (BaseLevel*3)
  self.health=5*BaseLevel
