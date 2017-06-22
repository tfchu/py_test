'''
Demonstrate "encapsulate what varies"
-> parts that varies easily in a class are moved to independent concrete classes
Composition class defines the layout of an article
Component class defines the component type (either graph or text)
Compositor abstract base class (or interface), defines the common methods for all compositors
    DefaultCompositor, TextCompositor inherits/implements the abc
When a new compositor is needed (for new component)
    1. add new compositor class, e.g. NewCompositor()
    2. in main()
        2.1. add the new component to component list
        2.2. add if statement to determine the new component type and its corresponding compositor
'''
from abc import ABCMeta, abstractmethod
from enum import Enum

#compositors
class Compositor(metaclass=ABCMeta):
    '''abstract base class as base to all compositors'''
    @abstractmethod
    def compose(self):
        '''abstract method compose(), defines how a component is composed'''
        pass

class DefaultCompositor(Compositor):
    '''default compositor'''
    def compose(self):
        print('Using default compositor')

class TextCompositor(Compositor):
    '''Text compositor'''
    def compose(self):
        print('Using text compositor')

class NewCompositor(Compositor):
    '''newly added compositor'''
    def compose(self):
        print('Using new compositor')

#component
class ComponentType(Enum):
    '''component types'''
    text = 1
    graph = 2
    new = 3

class Component(object):
    '''the component used in the composition'''
    def __init__(self, component_type):
        self.type = component_type

#composition
class Composition(object):
    '''the entire composition components and layout'''
    def __init__(self):
        self.compositor = None
        self.components = []
    def add_component(self, component):
        '''add new component to the composition'''
        self.components.append(component)
    def set_compositor(self, compositor):
        '''dynamically set the compositor type'''
        self.compositor = compositor
    def arranges(self):
        '''decides the layout based on component type'''
        self.compositor.compose()

def main():
    '''test the code'''
    composition = Composition()

    composition.add_component(Component(ComponentType.graph))
    composition.add_component(Component(ComponentType.text))
    composition.add_component(Component(ComponentType.new))
    composition.add_component(Component(ComponentType.text))

    for component in composition.components:
        if component.type == ComponentType.graph:
            composition.set_compositor(DefaultCompositor())
        elif component.type == ComponentType.text:
            composition.set_compositor(TextCompositor())
        elif component.type == ComponentType.new:
            composition.set_compositor(NewCompositor())
        else:
            composition.set_compositor(DefaultCompositor())
        composition.arranges()

if __name__ == '__main__':
    main()
    