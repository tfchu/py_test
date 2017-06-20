from abc import ABCMeta, abstractmethod

class Compositor(metaclass=ABCMeta):
    @abstractmethod
    def compose(self):
        pass

class SimpleComposior(Compositor):
    def compose(self):
        print('Simple compositor')

class TextCompositor(Compositor):
    def compose(self):
        print('Text compositor')

#add new compositor
class NewCompositor(Compositor):
    def compose(self):
        print('New compositor')

class Composition(object):
    def arranges(self, compositor):
        compositor.compose()

def main():
    composition = Composition()
    composition.arranges(SimpleComposior())
    composition.arranges(TextCompositor())
    composition.arranges(NewCompositor())

if __name__ == '__main__':
    main()
    