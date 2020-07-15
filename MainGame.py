from monsters import *
from player import *
from pet import *
from Leaving import *
from GUI import *
import time
import StoryFactsData as sf

def capture(Player,PetName):
    pet=Pet(PetName,Player.baselevel)
    gui=GUI(Player,'_')
    gui.CapturePet(pet)
    
def MonsterAttack(mon, PLAYER):
    if mon.name in sf.Bosses:
        damage=mon.attack+random.randint(0,3*Baselevel)
        print(
            f'{mon.name} a {mon.classt} type Boss monster attacks you!\nThey dealt {damage} damage')
    else:
        print(f'{mon.name} attacked you!')
    PLAYER.health -= damage


def attack(PLAYER, mon):
    print(f'{mon.name} a {mon.classt} type monster gets ready to fight you!')
    print(f'{PLAYER.name}:  Health:{PLAYER.health} Class:{PLAYER.classt} Element:{PLAYER.element}')
    print(f'{mon.name}:  Health:{mon.health} Class:{mon.classt}')
    time.sleep(2)
    gui = GUI(PLAYER, mon)
    while mon.health > 0 and PLAYER.health > 0:
        gui.options()
        MonsterAttack(mon, PLAYER)
        print(
            f'\n{mon.name}: Health:{mon.health}\n{PLAYER.name}: Health:{PLAYER.health}')
    if mon.health > PLAYER.health:
        leave(mon.finish)
    else:
        print(f'\nYou were victorious against {mon.name}')
    mon.regenerate()
    PLAYER.health = 100


def story1(PLAYER, MONSTERS, BaseLevel):
    mon = random.choice(MONSTERS)
    attack(PLAYER, mon)


def MakeMonsters(BaseLevel):
    BaseLevel = int(BaseLevel)
    if BaseLevel == 5:
        BaseLevel = 25
    BaseLevel += 10
    Bettasimha = Monster('Bettasimha', 'Champion',
                         f'The Champion of Battle, King of {sf.Location}', BaseLevel, 'You were obliterated from existence!')
    Mon1 = Monster(sf.mons1, sf.monse1, sf.monsd1, BaseLevel, sf.fin1)
    Mon2 = Monster(sf.mons2, sf.monse2, sf.monsd2, BaseLevel, sf.fin2)
    Mon3 = Monster(sf.mons3, sf.monse3, sf.monsd3, BaseLevel, sf.fin3)
    Mon4 = Monster(sf.mons4, sf.monse4, sf.monsd4, BaseLevel, sf.fin4)
    Mon5 = Monster(sf.mons5, sf.monse5, sf.monsd5, BaseLevel, sf.fin5)
    Mon6 = Monster(sf.mons6, sf.monse6, sf.monsd6, BaseLevel, sf.fin6)
    Mon7 = Monster(sf.mons7, sf.monse7, sf.monsd7, BaseLevel, sf.fin7)
    monsters = [Bettasimha, Mon1, Mon2, Mon3, Mon4, Mon5, Mon6, Mon7]
    return monsters


def main():
    gameName = sf.gameName
    classes = sf.classes
    elements = sf.elements
    print(f'Welcome to {gameName}')
    name = input('Enter Player name:')
    print(f'The classes available are:{classes}')
    classt = input('Enter prefered Class:').capitalize()
    if classt not in classes:
        print('Invalid class')
        leave('entered the wrong credentials')
    else:
        print(f'The elements available are:{elements}')
        element = input('Enter prefered Element:').capitalize()
        if element not in elements:
            print('Invalid element')
            leave('entered the wrong credentials')
    try:
        PLAYER = Player(name, classt, element)
    except:
        pass
    BaseLevel = input(
        'What level Would you like to play at, we include Easy ->Insane ?(1-5)')
    print(
        f'\nWelecome {PLAYER.name}\nWe are starting the {gameName} please wait while this happens')
    MONSTERS = MakeMonsters(BaseLevel)
    story1(PLAYER, MONSTERS, BaseLevel)
def NameMaker(alphabet):
 name=''
 for _ in range(4,random.randint(5,10)):
  name+=random.choice(alphabet)
 name=name.capitalize()
 return name

# def makeamon():
 alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','o','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 mon_disc=['an average monster','a normal monster']
 mon=Monster(NameMaker(alphabet),random.choice(['Fire','Water','Earth','Wind']),random.choice(mon_disc),1,'have been killed')
 return mon

if __name__ == '__main__':
    #  main()

    #  # testing
    gui=GUI('x','z')
    gui.Homescreen()
    # PLAYER = Player('Testing', 'Mage', 'Fire',1)
    # MONSTERS = MakeMonsters(1)
    # mon = random.choice(MONSTERS)
    # m=makeamon()
    # print(m.name)
    # attack(PLAYER, mon)
    # capture(PLAYER,NameMaker(['a','b','c','d','e']))
#  gui=GUI(PLAYER,mon)
#  print(mon.health)
#  gui.options()
#  print(mon.health)
# #  story1(PLAYER,MONSTERS)
