from abc import ABCMeta, abstractmethod

class ABCDocument(metaclass=ABCMeta):
    @abstractmethod
    def open_doc(self):
        pass
    @abstractmethod
    def read_line(self):
        pass
class WordDoc(ABCDocument):
    def open_doc(self):
        print('Word document opened')
    def read_line(self):
        print('one line of word document is read')
class HTMLDoc(ABCDocument):
    def open_doc(self):
        print('HTML document opened')
    def read_line(self):
        print('one line of HTML document is read')

class App(object):
    def __init__(self):
        self.doc = self.create_doc()
        self.doc.open_doc()
        self.doc.read_line()
    def create_doc(self):
        '''the factory method'''
        pass
class WordApp(App):
    def __init__(self):
        App.__init__(self)
    def create_doc(self):
        '''sub-class instantiates the object'''
        return WordDoc()
class HTMLApp(App):
    def __init__(self):
        App.__init__(self)
    def create_doc(self):
        '''sub-class instantiates the object'''
        return HTMLDoc()

def main():
    word_app = WordApp()
    html_app = HTMLApp()

if __name__ == '__main__':
    main()
