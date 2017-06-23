'''
Requirements:
    1. 4 kinds of ducks - Mallard, Redhead, Rubber, Decoy
    2. all can swim
    3. all look different
    4. fly modes: cannot fly, with wings, ... (more)
    5. sound: quake, squeak, silent, ... (more)
    6. during runtime, able to change fly mode and sound
Apply as many design principals
'''
from abc import ABCMeta, abstractmethod

#Ducks
class BaseDuck():
    def __init__(self):
        self.display = ''
        self.fly_modes = []
        self.sounds = []
    def swim(self):
        print('im swimming')
    def set_fly_mode(self, fly_mode):
        self.fly_modes.append(fly_mode)
    def set_sound(self, sound):
        self.sounds.append(sound)
    def switch_fly_mode(self, fly_mode):
        for mode in self.fly_modes:
            if mode.name == fly_mode.name:
                mode.switch()
                return
        print('fly mode not found')
    def switch_sound(self, sound):
        for snd in self.sounds:
            if snd.name == sound.name:
                snd.switch()
                return
        print('sound not found')
class MallardDuck(BaseDuck):
    def __init__(self):
        BaseDuck.__init__(self)
        self.display = 'Mallard Duck'
class RedheadDuck(BaseDuck):
    def __init__(self):
        BaseDuck.__init__(self)
        self.display = 'Readhead Duck'
#Fly modes
class ABCFlyMode(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass
class FlyWithWings(ABCFlyMode):
    def __init__(self):
        self.name = 'fly with wings'
    def switch(self):
        print('switch to fly with wings')
class FlyWithGadget(ABCFlyMode):
    def __init__(self):
        self.name = 'fly with gadget'
    def switch(self):
        print('swith to fly with gadget')
#Sounds
class ABCSound(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass
class Quake(ABCSound):
    def __init__(self):
        self.name = 'Quake'
    def switch(self):
        print('Quake Quake Quake')
class Squeak(ABCSound):
    def __init__(self):
        self.name = 'Squeak'
    def switch(self):
        print('Squeak Squeak Squeak')
class Silent(ABCSound):
    def __init__(self):
        self.name = 'Silent'
    def switch(self):
        print('Keep Quiet')
#selector
class Selector(object):
    def __init__(self, duck):
        self.duck = duck
        print(duck.display + ' is selected!')

def main():
    #init duck
    duck = MallardDuck()
    duck.set_fly_mode(FlyWithWings())
    duck.set_sound(Silent())
    duck.set_sound(Squeak())
    #choose a duck
    selector = Selector(duck)
    #go swimming
    selector.duck.swim()
    #switch fly mode
    selector.duck.switch_fly_mode(FlyWithWings())
    selector.duck.switch_fly_mode(FlyWithGadget())
    #switch sound
    selector.duck.switch_sound(Quake())
    selector.duck.switch_sound(Squeak())
    selector.duck.switch_sound(Silent())

if __name__ == '__main__':
    main()
