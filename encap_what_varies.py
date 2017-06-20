'''
Demonstrate "encapsulate what varies"
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
        print('Default compositor')

class TextCompositor(Compositor):
    '''Text compositor'''
    def compose(self):
        print('Text compositor')

class NewCompositor(Compositor):
    '''newly added compositor'''
    def compose(self):
        print('New compositor')

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
        self.components = []
    def add_component(self, component):
        '''add new component to the composition'''
        self.components.append(component)
    def arranges(self, compositor):
        '''decides the layout based on component type'''
        compositor.compose()

def main():
    '''test the code'''
    composition = Composition()

    composition.add_component(Component(ComponentType.graph))
    composition.add_component(Component(ComponentType.text))
    composition.add_component(Component(ComponentType.new))
    composition.add_component(Component(ComponentType.text))

    for component in composition.components:
        if component.type == ComponentType.graph:
            compositor = DefaultCompositor()
        elif component.type == ComponentType.text:
            compositor = TextCompositor()
        elif component.type == ComponentType.new:
            compositor = NewCompositor()
        else:
            compositor = DefaultCompositor()
        composition.arranges(compositor)

if __name__ == '__main__':
    main()
    