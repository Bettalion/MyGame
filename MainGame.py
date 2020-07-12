from monsters import *
from player import *
from Leaving import *
from GUI import *
import time
import StoryFactsData as sf


def MonsterAttack(mon, PLAYER):
    if mon.name in sf.Bosses:
        print(
            f'{mon.name} a {mon.classt} type Boss monster attacks you!\nThey dealt {mon.attack} damage')
    else:
        print(f'{mon.name} attacked you!')
    PLAYER.health -= mon.attack


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


if __name__ == '__main__':
    #  main()

    #  # testing
    PLAYER = Player('Testing', 'Mage', 'Fire')
    MONSTERS = MakeMonsters(1)
    mon = random.choice(MONSTERS)
    attack(PLAYER, mon)
#  gui=GUI(PLAYER,mon)
#  print(mon.health)
#  gui.options()
#  print(mon.health)
# #  story1(PLAYER,MONSTERS)
