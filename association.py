'''
demonstrate association
X knows Y, long term relationship
Y is used as class attribute
'''
class Author(object):
    '''contain information about the book author'''
    def __init__(self, name):
        self.name = name
    def get_name(self):
        '''return the author name'''
        return self.name

class Book(object):
    '''contain information about the book'''
    def __init__(self):
        #Association: Book knows Author, long term relationship
        #authors is a list of author objects
        self.authors = []
    def add_author(self, author):
        '''add author object to the author list'''
        self.authors.append(author)
    def list_authors(self):
        '''list all authors of the book'''
        for author in self.authors:
            print(author.get_name())

def main():
    '''main function to print name of all authors of a book'''
    book = Book()
    book.add_author(Author('Tony'))
    book.add_author(Author('Alice'))
    book.list_authors()

if __name__ == "__main__":
    main()
